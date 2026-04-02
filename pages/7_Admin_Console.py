import streamlit as st
import datetime
import json
from config.languages import CONTENT
from utils.session_init import init_session_state
from utils.helpers import load_all_global_css
from components.navbar import render_navbar
from components.footer import render_footer
from core.db_engine import db
from core.models import User, Vendor, Property, Booking

st.set_page_config(page_title="Admin Console", layout="wide")
init_session_state()
load_all_global_css()

if "lang" in st.query_params:
    st.session_state.lang = st.query_params["lang"]
elif 'lang' not in st.session_state:
    st.session_state.lang = 'vi'

L = CONTENT.get(st.session_state.lang, {})
render_navbar(current_page_path="/Admin_Console")

# Admin check (simple placeholder)
admin_emails = ['admin@vnwander.vn']
if 'user_email' not in st.session_state or st.session_state.get('user_email') not in admin_emails:
    st.error("Access denied. Admin login required.")
    st.stop()

session = db.get_session()
try:
    menu = ["Dashboard", "Property Approvals", "User Management", "Reports"]
    choice = st.sidebar.selectbox("Admin Menu", menu)

    if choice == "Dashboard":
        st.title("Admin Dashboard")
        # KPI cards
        total_bookings = session.query(Booking).count()
        total_revenue = session.query(Booking.total_price).filter(Booking.status == 'confirmed').all()
        total_revenue_sum = sum(r[0] for r in total_revenue) if total_revenue else 0
        total_properties = session.query(Property).count()
        total_users = session.query(User).count()
        pending_properties = session.query(Property).filter_by(is_active=False).count()

        col1, col2, col3, col4 = st.columns(4)
        col1.metric(L.get('total_revenue', 'Total Revenue'), f"{total_revenue_sum:,.0f} VND")
        col2.metric(L.get('total_bookings', 'Total Bookings'), total_bookings)
        col3.metric(L.get('total_properties', 'Properties'), total_properties)
        col4.metric(L.get('total_users', 'Users'), total_users)

        st.subheader(L.get('pending_approvals', 'Pending Property Approvals'))
        pending = session.query(Property).filter_by(is_active=False).all()
        if pending:
            for p in pending:
                col1, col2, col3 = st.columns([3,1,1])
                col1.write(f"{p.name} - {p.city}")
                if col2.button(L.get('approve', 'Approve'), key=f"approve_{p.id}"):
                    p.is_active = True
                    session.commit()
                    st.success(f"Property {p.name} approved!")
                    st.experimental_rerun()
                if col3.button(L.get('reject', 'Reject'), key=f"reject_{p.id}"):
                    session.delete(p)
                    session.commit()
                    st.warning(f"Property {p.name} rejected and removed.")
                    st.experimental_rerun()
        else:
            st.info(L.get('no_pending', 'No pending properties.'))

    elif choice == "Property Approvals":
        st.title(L.get('property_approvals', 'Property Approvals'))
        pending = session.query(Property).filter_by(is_active=False).all()
        for p in pending:
            with st.expander(f"{p.name} - {p.city}"):
                st.write(f"**Vendor:** {p.vendor.user.business_name}")
                st.write(f"**Address:** {p.address}")
                st.write(f"**Description:** {p.description}")
                st.write(f"**Amenities:** {', '.join(p.amenities) if p.amenities else 'None'}")
                col1, col2 = st.columns(2)
                if col1.button(L.get('approve', 'Approve'), key=f"approve2_{p.id}"):
                    p.is_active = True
                    session.commit()
                    st.success(f"Property {p.name} approved!")
                    st.experimental_rerun()
                if col2.button(L.get('reject', 'Reject'), key=f"reject2_{p.id}"):
                    session.delete(p)
                    session.commit()
                    st.warning(f"Property {p.name} rejected.")
                    st.experimental_rerun()

    elif choice == "User Management":
        st.title(L.get('user_management', 'User Management'))
        users = session.query(User).all()
        user_data = []
        for u in users:
            role = 'vendor' if u.vendor else u.role
            user_data.append({
                "ID": u.id,
                "Email": u.email,
                "Name": u.full_name,
                "Phone": u.phone,
                "Role": role,
                "Active": u.is_active
            })
        st.dataframe(user_data)
        st.subheader(L.get('suspend_user', 'Suspend/Activate User'))
        user_id = st.number_input("User ID", min_value=1, step=1)
        if st.button(L.get('toggle_status', 'Toggle Active Status')):
            u = session.query(User).get(user_id)
            if u:
                u.is_active = not u.is_active
                session.commit()
                st.success(f"User {u.email} active status changed to {u.is_active}")
            else:
                st.error("User not found")

    elif choice == "Reports":
        st.title(L.get('reports', 'Reports'))
        # Simple GMV chart
        import matplotlib.pyplot as plt
        # Group bookings by month
        bookings = session.query(Booking).filter(Booking.status == 'confirmed').all()
        monthly = {}
        for b in bookings:
            month = b.created_at.strftime('%Y-%m')
            monthly[month] = monthly.get(month, 0) + b.total_price
        months = sorted(monthly.keys())
        values = [monthly[m] for m in months]
        fig, ax = plt.subplots()
        ax.plot(months, values, marker='o')
        ax.set_title(L.get('gmv_trend', 'Gross Merchandise Value (GMV) Trend'))
        ax.set_xlabel(L.get('month', 'Month'))
        ax.set_ylabel(L.get('amount_vnd', 'Amount (VND)'))
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Export data (JSON)
        if st.button(L.get('export_bookings', 'Export Bookings (JSON)')):
            bookings_data = []
            for b in bookings:
                bookings_data.append({
                    "reference": b.booking_reference,
                    "guest": b.user.full_name,
                    "property": b.property.name,
                    "check_in": b.check_in.strftime('%Y-%m-%d'),
                    "check_out": b.check_out.strftime('%Y-%m-%d'),
                    "total": float(b.total_price)
                })
            with open("data/bookings_export.json", "w", encoding='utf-8') as f:
                json.dump(bookings_data, f, ensure_ascii=False, indent=2)
            st.success(L.get('export_success', 'Export saved to data/bookings_export.json'))

except Exception as e:
    st.error(f"Error: {str(e)}")
finally:
    session.close()

render_footer()
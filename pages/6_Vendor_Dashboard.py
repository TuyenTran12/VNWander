import streamlit as st
import datetime
from components.ai_widget import render_chat_widget
from config.languages import CONTENT
from utils.session_init import init_session_state
from utils.helpers import load_all_global_css
from components.navbar import render_navbar
from components.footer import render_footer
from core.db_engine import db
from core.models import Vendor, Property, Room, Inventory, Booking

st.set_page_config(page_title="Vendor Dashboard", layout="wide")
init_session_state()
load_all_global_css()

if "lang" in st.query_params:
    st.session_state.lang = st.query_params["lang"]
elif 'lang' not in st.session_state:
    st.session_state.lang = 'vi'

L = CONTENT.get(st.session_state.lang, {})
render_navbar(current_page_path="/Vendor_Dashboard")

# For demo, assume a logged-in vendor. In real app, get from session.
# We'll use a placeholder vendor id (1)
vendor_id = 1

session = db.get_session()
try:
    vendor = session.query(Vendor).filter_by(id=vendor_id).first()
    if not vendor:
        st.error("Vendor not found. Please login.")
        st.stop()
    properties = session.query(Property).filter_by(vendor_id=vendor.id).all()
    if not properties:
        st.info("You have no properties. Contact admin to add one.")
        st.stop()

    # Sidebar navigation
    menu = ["Dashboard", "Inventory Manager", "Bookings", "Property Settings"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Dashboard":
        st.title("Dashboard")
        total_bookings = 0
        total_revenue = 0
        upcoming_checkins = 0
        for prop in properties:
            bookings = session.query(Booking).filter_by(property_id=prop.id, status='confirmed').all()
            total_bookings += len(bookings)
            total_revenue += sum(b.total_price for b in bookings)
            upcoming = session.query(Booking).filter(
                Booking.property_id == prop.id,
                Booking.check_in.between(datetime.date.today(), datetime.date.today() + datetime.timedelta(days=3))
            ).count()
            upcoming_checkins += upcoming

        col1, col2, col3, col4 = st.columns(4)
        col1.metric(L.get('total_bookings', 'Total Bookings'), total_bookings)
        col2.metric(L.get('total_revenue', 'Revenue'), f"{total_revenue:,.0f} VND")
        col3.metric(L.get('upcoming_checkins', 'Upcoming Check-ins'), upcoming_checkins)
        col4.metric(L.get('properties', 'Properties'), len(properties))

        # Recent bookings table
        st.subheader(L.get('recent_bookings', 'Recent Bookings'))
        recent = session.query(Booking).filter(Booking.property_id.in_([p.id for p in properties])).order_by(Booking.created_at.desc()).limit(10).all()
        if recent:
            data = []
            for b in recent:
                room = session.query(Room).get(b.room_id)
                data.append({
                    "Reference": b.booking_reference,
                    "Guest": b.user.full_name,
                    "Room": room.name if room else "N/A",
                    "Check-in": b.check_in.strftime('%Y-%m-%d'),
                    "Check-out": b.check_out.strftime('%Y-%m-%d'),
                    "Status": b.status,
                    "Total": f"{b.total_price:,.0f} VND"
                })
            st.table(data)
        else:
            st.info(L.get('no_recent_bookings', 'No recent bookings.'))

    elif choice == "Inventory Manager":
        st.title(L.get('inventory_manager', 'Inventory Manager'))
        for prop in properties:
            st.subheader(prop.name)
            rooms = session.query(Room).filter_by(property_id=prop.id).all()
            for room in rooms:
                st.markdown(f"**{room.name}**")
                start_date = datetime.date.today()
                end_date = start_date + datetime.timedelta(days=30)
                inv_data = {}
                invs = session.query(Inventory).filter(
                    Inventory.room_id == room.id,
                    Inventory.date.between(start_date, end_date)
                ).all()
                for inv in invs:
                    inv_data[inv.date] = inv.available_rooms

                cols = st.columns(7)
                days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                for i, day in enumerate(days):
                    cols[i].markdown(f"**{day}**")
                current = start_date
                while current <= end_date:
                    week_col = current.weekday()
                    with cols[week_col]:
                        avail = inv_data.get(current, 3)
                        new_avail = st.number_input(f"{current.strftime('%d/%m')}", min_value=0, max_value=10, value=avail, key=f"inv_{room.id}_{current}")
                        if new_avail != avail:
                            inv = session.query(Inventory).filter_by(room_id=room.id, date=current).first()
                            if inv:
                                inv.available_rooms = new_avail
                            else:
                                inv = Inventory(room_id=room.id, date=current, available_rooms=new_avail)
                                session.add(inv)
                    current += datetime.timedelta(days=1)
                st.markdown("---")
        if st.button(L.get('save_changes', 'Save Changes')):
            session.commit()
            st.success(L.get('inventory_updated', 'Inventory updated!'))

    elif choice == "Bookings":
        st.title(L.get('all_bookings', 'All Bookings'))
        all_bookings = session.query(Booking).filter(Booking.property_id.in_([p.id for p in properties])).order_by(Booking.created_at.desc()).all()
        if all_bookings:
            data = []
            for b in all_bookings:
                room = session.query(Room).get(b.room_id)
                data.append({
                    "Reference": b.booking_reference,
                    "Guest": b.user.full_name,
                    "Room": room.name if room else "N/A",
                    "Check-in": b.check_in.strftime('%Y-%m-%d'),
                    "Check-out": b.check_out.strftime('%Y-%m-%d'),
                    "Guests": b.guest_count,
                    "Status": b.status,
                    "Payment": b.payment_status,
                    "Total": f"{b.total_price:,.0f} VND",
                    "Special Requests": b.special_requests[:50] if b.special_requests else ""
                })
            st.dataframe(data)
        else:
            st.info(L.get('no_bookings', 'No bookings yet.'))

    elif choice == "Property Settings":
        st.title(L.get('property_settings', 'Property Settings'))
        for prop in properties:
            with st.expander(prop.name):
                new_name = st.text_input(L.get('name', 'Name'), value=prop.name, key=f"prop_name_{prop.id}")
                new_desc = st.text_area(L.get('description', 'Description'), value=prop.description or "", key=f"prop_desc_{prop.id}")
                new_policies = st.text_area(L.get('policies', 'Policies'), value=prop.policies or "", key=f"prop_policies_{prop.id}")
                st.subheader(L.get('rooms', 'Rooms'))
                for room in prop.rooms:
                    col1, col2 = st.columns(2)
                    with col1:
                        new_room_name = st.text_input(L.get('room_name', 'Room Name'), value=room.name, key=f"room_name_{room.id}")
                        new_room_max = st.number_input(L.get('max_occupancy', 'Max Occupancy'), min_value=1, value=room.max_occupancy, key=f"room_max_{room.id}")
                    with col2:
                        new_room_price = st.number_input(L.get('price_per_night', 'Price per night (VND)'), min_value=0, value=int(room.price_per_night), key=f"room_price_{room.id}")
                        new_room_bed = st.text_input(L.get('bed_config', 'Bed Configuration'), value=room.bed_configuration or "", key=f"room_bed_{room.id}")
                    if st.button(L.get('update_room', 'Update Room'), key=f"update_room_{room.id}"):
                        room.name = new_room_name
                        room.max_occupancy = new_room_max
                        room.price_per_night = new_room_price
                        room.bed_configuration = new_room_bed
                        session.commit()
                        st.success(L.get('room_updated', 'Room updated!'))
                if st.button(L.get('update_property', 'Update Property'), key=f"update_prop_{prop.id}"):
                    prop.name = new_name
                    prop.description = new_desc
                    prop.policies = new_policies
                    session.commit()
                    st.success(L.get('property_updated', 'Property updated!'))
except Exception as e:
    st.error(f"Error: {str(e)}")
finally:
    session.close()

render_footer()
render_chat_widget()
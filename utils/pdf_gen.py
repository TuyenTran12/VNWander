import uuid
import os
from datetime import datetime
from fpdf import FPDF
from config.languages import CONTENT

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'VNWander', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_booking_voucher(booking_data, lang='vi'):
    """
    Generate a bilingual PDF voucher for a booking.
    booking_data: dict with keys: booking_reference, guest_name, property_name,
                  room_name, check_in, check_out, total_price, etc.
    Returns file path.
    """
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title
    pdf.set_font('Arial', 'B', 14)
    title = 'Booking Confirmation' if lang == 'en' else 'Xác nhận đặt phòng'
    pdf.cell(0, 10, title, 0, 1, 'C')
    pdf.ln(10)

    # Details
    pdf.set_font('Arial', '', 12)
    labels = {
        'en': {
            'ref': 'Booking Reference',
            'guest': 'Guest Name',
            'property': 'Property',
            'room': 'Room Type',
            'checkin': 'Check-in',
            'checkout': 'Check-out',
            'total': 'Total Amount',
            'status': 'Status'
        },
        'vi': {
            'ref': 'Mã đặt phòng',
            'guest': 'Tên khách hàng',
            'property': 'Khách sạn',
            'room': 'Loại phòng',
            'checkin': 'Ngày nhận phòng',
            'checkout': 'Ngày trả phòng',
            'total': 'Tổng tiền',
            'status': 'Trạng thái'
        }
    }
    lbl = labels[lang]

    pdf.cell(50, 10, f"{lbl['ref']}:", 0, 0)
    pdf.cell(0, 10, booking_data['booking_reference'], 0, 1)
    pdf.cell(50, 10, f"{lbl['guest']}:", 0, 0)
    pdf.cell(0, 10, booking_data['guest_name'], 0, 1)
    pdf.cell(50, 10, f"{lbl['property']}:", 0, 0)
    pdf.cell(0, 10, booking_data['property_name'], 0, 1)
    pdf.cell(50, 10, f"{lbl['room']}:", 0, 0)
    pdf.cell(0, 10, booking_data['room_name'], 0, 1)
    pdf.cell(50, 10, f"{lbl['checkin']}:", 0, 0)
    pdf.cell(0, 10, booking_data['check_in'], 0, 1)
    pdf.cell(50, 10, f"{lbl['checkout']}:", 0, 0)
    pdf.cell(0, 10, booking_data['check_out'], 0, 1)
    pdf.cell(50, 10, f"{lbl['total']}:", 0, 0)
    pdf.cell(0, 10, booking_data['total_price'], 0, 1)
    pdf.cell(50, 10, f"{lbl['status']}:", 0, 0)
    pdf.cell(0, 10, booking_data['status'], 0, 1)

    # Additional info
    pdf.ln(10)
    pdf.set_font('Arial', 'I', 10)
    note = 'Thank you for choosing VNWander. Please present this voucher at check-in.' if lang == 'en' \
           else 'Cảm ơn bạn đã chọn VNWander. Vui lòng xuất trình phiếu này khi nhận phòng.'
    pdf.multi_cell(0, 10, note)

    # Save file
    filename = f"vouchers/{booking_data['booking_reference']}.pdf"
    os.makedirs('vouchers', exist_ok=True)
    pdf.output(filename)
    return filename
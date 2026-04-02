import locale
from datetime import datetime

def format_currency(amount, lang='vi'):
    """
    Format amount as VND with proper thousand separators.
    lang: 'vi' or 'en'
    """
    if lang == 'vi':
        return f"{amount:,.0f} ₫".replace(',', '.')
    else:
        return f"${amount:,.2f}".replace(',', ',')

def format_date(date_obj, lang='vi'):
    """
    Format date according to language.
    """
    if lang == 'vi':
        return date_obj.strftime('%d/%m/%Y')
    else:
        return date_obj.strftime('%Y-%m-%d')

def format_datetime(dt_obj, lang='vi'):
    """
    Format datetime with time.
    """
    if lang == 'vi':
        return dt_obj.strftime('%d/%m/%Y %H:%M')
    else:
        return dt_obj.strftime('%Y-%m-%d %H:%M')
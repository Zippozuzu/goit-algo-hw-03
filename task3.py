import re

def normalize_phone(phone_number):
    format_phone_number = (re.sub(r'[\D]','', phone_number))

    if format_phone_number.startswith('38'):
        format_phone_number = '+' + format_phone_number
    else:
        format_phone_number = '+38' + format_phone_number

    return format_phone_number


from datetime import datetime
from re import match


def is_date(field_value):
	# It's ugly, but it works. Can be improved with regular expressions
	try:
		datetime.strptime(field_value, "%Y-%m-%d")
		return True
	except ValueError:
		pass

	try:
		datetime.strptime(field_value, "%d.%m.%Y")
		return True
	except ValueError:
		pass

	return False


def is_phone(field_value):
	# It's ugly, but it works. Can be improved with regular expressions
	is_phone_number_part = lambda s, l: (len(s) == l) and s.isdigit()
	try:
		number_parts = field_value.split()
		checks = [ 
			len(number_parts) != 5,
			number_parts[0] != '+7',
			not is_phone_number_part(number_parts[1], 3),
			not is_phone_number_part(number_parts[2], 3),
			not is_phone_number_part(number_parts[3], 2),
			not is_phone_number_part(number_parts[4], 2)
		]

		if any(checks):
			return False
		return True
	except Exception:
		return False


def is_email(field_value):
	if match(r'[^@]+@[^@]+\.[^@]+', field_value):
		return True
	return False


def get_str_type(field_value):
	if is_date(field_value):
		return 'date'

	if is_phone(field_value):
		return 'phone'

	if is_email(field_value):
		return 'email'

	return 'text'

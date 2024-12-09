from datetime import datetime


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


def get_str_type(field_value):
	if is_date(field_value):
		return 'date'

	# if field_value ...:
	# 	return 'phone'

	# if field_value ...:
	# 	return 'email'

	return 'text'


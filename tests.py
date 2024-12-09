import unittest
from app import app, db
from validators import get_str_type


class UserModelCase(unittest.TestCase):
	def test_basic_responses(self):
		client = app.test_client()

		form_data = {'test_field_name': 'order_date', 'test_value' : '00.00.0000'}
		response = client.post('/get_form', json = form_data)
		self.assertTrue(response.status_code == 200)

		# Check the response for different numbers of field names
		form_data = {
			'test_field_name': 'order_date', 
			'test_value' : '00.00.0000', 
			'another_name': 'mail@mail.com'}
		response = client.post('/get_form', json = form_data)
		self.assertTrue(response.status_code == 400)

		form_data = {'test_field_name': 'order_date'}
		response = client.post('/get_form', json = form_data)
		self.assertTrue(response.status_code == 400)

	def test_validators(self):
		# Dates
		dates  = ['12.05.2018', '12.5.2018', '07.02.2020', '7.2.2020']
		dates += ['01.09.2021', '1.9.2021', '08.11.2022', '8.11.2022']
		for date in dates:
			self.assertTrue(
				get_str_type(date) == 'date'
			)

		not_dates = ['12_05.2018', '12.05.12.2018', '12-2018-05','2018-05-12-12']
		for noise in not_dates:
			self.assertFalse(
				get_str_type(noise) == 'date'
			)

		# Phones
		phones = ['+7 999 999 99 99', '+7 987 789 99 99', '+7 978 078 77 77']
		for phone in phones:
			self.assertTrue(
				get_str_type(phone) == 'phone'
			)

		not_phones  = ['-7 999 999 99 99', '+7 999 -99 9- 99', '+7 9a9 999 99 b9']
		not_phones += ['+7 999 999 99 99 893', '+7 999 888', '+7 90 99 99 999 99']
		for noise in not_phones:
			self.assertFalse(
				get_str_type(noise) == 'phone'
			)

		# Emails
		emails = ['mail@gmail.com', 'full@example.com', 'example@whatever.com']
		for email in emails:
			self.assertTrue(
				get_str_type(email) == 'email'
			)

		not_emails = ['wrong@example,com', 'wrong-example', 'wrong@', '@example.com']
		for noise in not_emails:
			self.assertFalse(
				get_str_type(noise) == 'email'
			)

		# Texts
		texts = not_dates + not_phones + not_emails
		for text in texts:
			self.assertTrue(
				get_str_type(text) == 'text'
			)

	def test_search_function(self):
		client = app.test_client()

		# 2 form names
		form_data = {'user_name': 'the end', 'order_date' : '09.12.2024'}
		response = client.post('/get_form', json = form_data)
		self.assertEqual(response.get_json(),
			{'result': ['Order Form', 'Order Form with phone number']}
		) 

		# a single form name
		form_data = {'user_name': 'the end', 'number' : '+7 123 456 78 90'}
		response = client.post('/get_form', json = form_data)
		self.assertEqual(response.get_json(),
			{'result': ['Order Form with phone number']}
		) 
		# another one
		form_data = {'user_name': 'the end', 'lead_email' : 'completed@task.com'}
		response = client.post('/get_form', json = form_data)
		self.assertEqual(response.get_json(),
			{'result': ['Order Form']}
		)

		# no name at all
		form_data = {'user_nickname': 'name', 'OrderDate' : '09.12.2024'}
		response = client.post('/get_form', json = form_data)
		self.assertEqual(response.get_json(),
			{'user_nickname': 'text', 'OrderDate' : 'date'}
		)


if __name__ == '__main__':
	unittest.main(verbosity=2)

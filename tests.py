import unittest
from app import app, db
from validators import get_str_type


class UserModelCase(unittest.TestCase):
	def test_basic_response(self):
		client = app.test_client()

		form_data = {'test_field_name': 'order_date', 'test_value' : '00.00.0000'}

		response = client.post('/get_form', json = form_data)
		self.assertTrue(response.status_code == 200)

		print(response.text)

		self.assertTrue(
			response.get_json()['message'] == 'Hello, world!'
		)

	def test_validators(self):
		dates  = ['12.05.2018', '12.5.2018', '07.02.2020', '7.2.2020']
		dates += ['01.09.2021', '1.9.2021', '08.11.2022', '8.11.2022']
		for date in dates:
			self.assertTrue(
				get_str_type(date) == 'date'
			)

		not_dates = ['test', '+7 999 999 99 99', 'mail@gmail.com']
		for noise in not_dates:
			self.assertFalse(
				get_str_type(noise) == 'date'
			)


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


if __name__ == '__main__':
	unittest.main(verbosity=2)

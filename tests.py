import unittest
from app import app, db


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


if __name__ == '__main__':
	unittest.main(verbosity=2)

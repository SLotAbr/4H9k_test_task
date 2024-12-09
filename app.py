from flask import Flask, request
from werkzeug.http import HTTP_STATUS_CODES
from tinydb import TinyDB


app = Flask(__name__)
app.config['TINYDB_PATH'] = 'db.json'
db = TinyDB(app.config['TINYDB_PATH'])


@app.route('/get_form', methods=['POST'])
def get_form():
	# print(request.get_json())
	# print(request.args)
	# we should return json as well
	# test-driven development

	# a place for search functionality

	# a place for an 'else' condition

	# We're expecting only 2 field_names
	if len(request.get_json().items()) != 2:
		payload = {'error': HTTP_STATUS_CODES.get(400)}
		return payload, 400

	return {'message':"Hello, world!"}

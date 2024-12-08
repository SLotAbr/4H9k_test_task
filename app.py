from flask import Flask, request
from tinydb import TinyDB


app = Flask(__name__)
app.config['TINYDB_PATH'] = 'db.json'
db = TinyDB(app.config['TINYDB_PATH'])


@app.route('/get_form', methods=['POST'])
def get_form():
	# print(request.get_json())
	print(request.args)

	# we should return json as well
	# test-driven development
	return {'message':"Hello, world!"}

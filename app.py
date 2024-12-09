from flask import Flask, request
from werkzeug.http import HTTP_STATUS_CODES
from tinydb import TinyDB, Query
from validators import get_str_type


app = Flask(__name__)
app.config['TINYDB_PATH'] = 'db.json'
db = TinyDB(app.config['TINYDB_PATH'])


@app.route('/get_form', methods=['POST'])
def get_form():
	# We're expecting only 2 field_names
	fields = request.get_json()
	if len(fields.items()) != 2:
		payload = {'error': HTTP_STATUS_CODES.get(400)}
		return payload, 400

	# test-driven development

	keys = list(fields.keys())
	parameters = { 
		keys[0]: get_str_type(fields[keys[0]]),  
		keys[1]: get_str_type(fields[keys[1]])
	}

	query = Query()
	entries = db.search(
		(query[keys[0]]==parameters[keys[0]]) &\
		(query[keys[1]]==parameters[keys[1]])
	)
	if entries:
		return {'result': [e['name'] for e in entries]}
	else:
		return parameters

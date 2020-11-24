from flask import Flask, jsonify, abort, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='/templates')
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///department_manager.db'
db = SQLAlchemy(app)


dummy = [
	{'id': 1, 'name': 'IT'},
	{'id': 2, 'name': 'Marketing'},
	{'id': 3, 'name': 'HR'},
	{'id': 4, 'name': 'R&D'},
	{'id': 5, 'name': 'Accounting and Finance'},
	{'id': 6, 'name': 'Purchasing'},
	{'id': 7, 'name': 'Planning'},
	{'id': 8, 'name': 'Technical Dept.'}
]


@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/test')
def ci_test():
	return 'Time to test CI'


class Departments(Resource):
	'''
	Flask-RESTful class to implement CRUD methods
	'''
	def get(self, department_id):
		if department_id <= 0:
			abort(403, description="Id's should start from 1")
		departments = [department for department in dummy if department['id'] == department_id]
		return jsonify(departments[0])

	def put(self, department_id):
		departments = [department for department in dummy if department['id'] == department_id]
		if department_id <= 0:
			abort(403, description="Id's should start from 1")
		if len(departments) == 0:
			abort(404)
		if not request.json:
			abort(404)
		if not isinstance(request.json['id'], int):
			abort(403, description="Id's should be integers")


		return 'PUT Success'


api.add_resource(Departments, '/api/departments/<int:department_id>')


if __name__ == '__main__':
	app.run(debug=True)

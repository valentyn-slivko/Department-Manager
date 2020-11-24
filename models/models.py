from main import db


class Department(db.Model):
	id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
	department_name = db.Column(db.String(100), nullable=False)
	employees = db.relationship('Employee', backref='employee')


class Employee(db.Model):
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(100), nullable=False)
	surname = db.Column(db.String(100), nullable=False)
	related_department_id = db.relationship(db.Integer, db.ForeignKey('department.id'))
	date_of_birth = db.Column(db.String(10), nullable=False)
	salary = db.Column(db.Integer)

	def __repr__(self):
		return f'Employee: {Employee.name} {Employee.surname}, with salary: {Employee.salary}$, born at {Employee.date_of_birth}, working at {Department.department}'

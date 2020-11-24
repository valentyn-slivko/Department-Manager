import unittest
import requests

PATH = 'http://localhost:5000/'


class ApiTestCase(unittest.TestCase):
	def test_get_method(self):
		response = requests.get(PATH + 'api/departments/2')
		assert response.headers['Content-Type'] == 'application/json'
		response_body = response.json()
		assert response_body['id'] == 2

	def test_put_method(self):
		response = requests.put(PATH + 'api/departments/9', data={'id': 9, 'department': 'Another one'}).json()


import unittest
from main import hello_world


class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(hello_world(), 'Hello World!')


if __name__ == '__main__':
	unittest.main()

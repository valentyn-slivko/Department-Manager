import unittest
from main import hello_world, ci_test


class MyTestCase(unittest.TestCase):
	def test_hello_world(self):
		self.assertEqual(hello_world(), 'Hello World!')

	def test_ci_build(self):
		self.assertEqual(ci_test(), 'Time to test CI')


if __name__ == '__main__':
	unittest.main()

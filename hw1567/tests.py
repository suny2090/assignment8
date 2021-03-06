import unittest
from investment import *

class tests(unittest.TestCase):

	"""Unit-testing class that allows us to run tests with expected outcomes
	Run the test in the project's root directory
	with the following command:
		$ python -m unittest discover
	"""
	def test_constructor(self):

	#unit tests for the investment constructor that pass input to 
	#arguments positoins and num_trials

		self.assertEqual(investment([1, 10, 100], 1000).positions, [1, 10, 100])
		self.assertEqual(investment([1, 10, 100], 1000).num_trials, 1000)

	def test_stimulate(self):

		"""unit tests for testing stimulate method.
			We test the each value of the return dictionary 'result' has the same length as
			num_trials, and every element in the value of dictionary 'result' bigger than 
			or equal to -1, and less than or equal to 1 
		"""
		a = investment([1, 10, 100], 1000)
		result = a.stimulate([1000.0, 100.0, 10.0], 1000) 

		self.assertEqual(len(result[1]), 1000)
		self.assertEqual(len(result[10]), 1000)
		self.assertEqual(len(result[100]), 1000)

		self.assertTrue(result[1].all() <= 1)
		self.assertTrue(result[1].all() >= -1)

		self.assertTrue(result[10].all() <= 1)
		self.assertTrue(result[10].all() >= -1)

		self.assertTrue(result[100].all() <= 1)
		self.assertTrue(result[100].all() >= -1)

if __name__ == "__main__":
    unittest.main()
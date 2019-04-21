import unittest
from linear_search import linearSearch
from binary_search import binarySearch

class SearchTestCase(unittest.TestCase):
	
	# Tests for linear search
	def testLinearSearch(self):
		values = [2, 1, 3 , 9, 5]
		self.assertEqual(linearSearch(values, 1), 1)
		self.assertEqual(linearSearch(values, 9), 3)
		self.assertEqual(linearSearch(values, 7), -1)

	# Tests for binary search
	def testBinarySearch(self):
		values = [1, 2, 3 , 4, 5]
		self.assertEqual(binarySearch(values, 1), 0)
		self.assertEqual(binarySearch(values, 4), 3)
		self.assertEqual(binarySearch(values, 7), -1)


if __name__ == '__main__':
	unittest.main()

import unittest
from main import search

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.arr = [9, 4, 8, 7, 0, 5]
        self.searched = [9, 4, 7]
    def test_search(self):
        self.assertEqual(self.searched, search(self.arr))

if __name__ == '__main__':
        unittest.main()
import unittest
from dataanalysis.analysis import *


class Testing(unittest.TestCase):
    def test_list_dict(self):
        result = list_dict('test.csv')
        expect = [{'date': '2020-1', 'resource': '1', 'count': '11'}, {'date': '2020-2', 'resource': '2', 'count': '22'}
            , {'date': '2020-3', 'resource': '3', 'count': '33'}]
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()

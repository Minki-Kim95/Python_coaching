import unittest
from week1 import Assignment2 as ass2


class TestAssignment1(unittest.TestCase):

    def test_different_cases(self):
        self.assertEqual(ass2.findcommon('abcd', 'abcd'), 'abcd')
        self.assertEqual(ass2.findcommon('abcd', 'efgh'), '')
        self.assertEqual(ass2.findcommon('abcde', 'abrty'), 'ab')
        self.assertEqual(ass2.findcommon('', ''), '')
        self.assertEqual(ass2.findcommon('vwahertnf', 'aberjhaag'), 'aehr')
        self.assertEqual(ass2.findcommon('aaaaaaa', 'abcde'), 'a')


if __name__ == '__main__':
    unittest.main()

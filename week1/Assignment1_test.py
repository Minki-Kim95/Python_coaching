# 길이를 입력 받아서 입력은 앞에서부터 출력은 뒤에서부터 읽으면서 체크하는 걸 만들면 될듯
# 근데 테스트중에 입력받는건 좀 이상하다 그냥 샘플로 하자

import unittest
from week1 import Assignment1 as hw1


class TestAssignment1(unittest.TestCase):

    def test_different_cases(self):
        self.assertEqual(hw1.convert('abcd'), 'dcba')
        self.assertEqual(hw1.convert('a'), 'a')
        self.assertEqual(hw1.convert('abcde'), 'edcba')
        self.assertEqual(hw1.convert(''), '')


if __name__ == '__main__':
    unittest.main()


import for_test

import mock
import unittest.mock

expression = ['2+3=5', '3*7=20', 'two plus three is five', '-0+1=1',
              '+4+4=8', '4+4 = 8', '4+4=8.0', '-5--7=-12', '-5+-7=-12',
              '6/5=1', '1/0=1', '-1-1=-1-1', '132+3=', '123+-3=126',
              '123/0=0', '1-1-1=2', '+3f+3+sg=3']


class Test(unittest.TestCase):
    @mock.patch('for_test.input')
    def test(self, input_mock):
        for exp in expression:
            input_mock.return_value = exp


if __name__ == '__main__':
    unittest.main()

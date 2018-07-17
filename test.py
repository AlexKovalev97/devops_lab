import for_test

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        """Init"""

    def test_checker(self):
        self.assertEqual(for_test.checker('2+3=5'), 'YES')
        self.assertEqual(for_test.checker('1+2=4'), 'NO')
        self.assertEqual(for_test.checker('1+3=5=2+3'), 'ERROR')

    def tearDown(self):
        """Finish"""


if __name__ == '__main__':
    unittest.main()

import for_test

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        """Init"""

    def test_checker(self):
            self.assertEqual(for_test.checker('2+3=5'), 'YES')

    def test_checker_2(self):
            self.assertEqual(for_test.checker('1+2=4'), 'NO')

    def test_checker_3(self):
            self.assertEqual(for_test.checker('1+3=5=2+3'), 'ERROR')

    def test_checker_4(self):
            self.assertEqual(for_test.checker('0123456789001234567890'
                                              '0123456789001234567890'
                                              '0123456789001234567890'
                                              '0123456789001234567890'
                                              '0123456789001234567890'
                                              '0123456789001234567890'), 'ERROR')

    def test_checker_5(self):
        self.assertEqual(for_test.checker('1.3+5=7'), 'ERROR')

    def tearDown(self):
        """Finish"""


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-

from .context import bade

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_kph_to_mph_conversion(self):
        speed = 10
        result = kph_to_mph(speed)
        self.assertEqual(result, speed*0.621)
        
    def test_mph_to_kph_conversion(self):
        speed = 10
        result = mph_to_kph(speed)
        self.assertEqual(result, speed/0.621)


if __name__ == '__main__':
    unittest.main()
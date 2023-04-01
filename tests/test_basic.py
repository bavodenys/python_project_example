# -*- coding: utf-8 -*-

from .context import bade

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_kph_to_knots_conversion(self):
        speed = 10
        result = bade.speedconversion.kph_to_knots(speed)
        self.assertEqual(result, speed*0.60)
        
    def test_knots_to_kph_conversion(self):
        speed = 10
        result = bade.speedconversion.knots_to_kph(speed)
        self.assertEqual(result, speed/0.54)


if __name__ == '__main__':
    unittest.main()

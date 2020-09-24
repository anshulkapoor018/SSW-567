#!/user_id/bin/env python

"""
HW01_Anshul_Kapoor.py
The primary goal of this file is to demonstrate a simple unittest implementation
"""
__author__ = "Anshul Kapoor"

from math import sqrt
import unittest

def classify_triangle(a, b, c):
    side1 = sqrt(a ** 2 + b ** 2)
    sideTotal = a + b + c
    if sideTotal < (2 * a) or sideTotal < (2 * b) or sideTotal < (2 * c):
        return "NotATriangle"
    if side1 == c:
        return "Right"

    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or c == a:
        return "Isosceles"
    else:
        return "Scalene"


def executeClassifyTriangle(a, b, c):
    print('classifyTriangle(', a, ',', b, ',', c, ') = ', classify_triangle(a, b, c), sep="")

def main():
    executeClassifyTriangle(20, 21, 29)
    executeClassifyTriangle(3, 4, 5)


class TestTriangles(unittest.TestCase):
    def testingSet1(self):
        self.assertEqual(classify_triangle(20, 21, 29), 'Right', '20, 21, 29 is a Right triangle')

    def testingSet2(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
        self.assertNotEqual(classify_triangle(12, 12, 12), 'Isosceles', 'Should be Equilateral')
        self.assertEqual(classify_triangle(7, 15, 30), 'NotATriangle', 'Should be not be a Triangle')


if __name__ == '__main__':
    main()
    # unittest.main(exit=False, verbosity=2)

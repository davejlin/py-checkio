'''
You are given the lengths for each side on a triangle. You need to
find all three angles for this triangle. If the given side lengths
cannot form a triangle (or form a degenerated triangle), then you must
return all angles as 0 (zero). The angles should be represented as a
list of integers in ascending order. Each angle is measured in degrees
and rounded to the nearest integer number (Standard mathematical
rounding).

triangle-angles

Input: The lengths of the sides of a triangle as integers.

Output: Angles of a triangle in degrees as sorted list of integers.

Example:

checkio(4, 4, 4) == [60, 60, 60]
checkio(3, 4, 5) == [37, 53, 90]
checkio(2, 2, 5) == [0, 0, 0]

How it is used: This is a classical geometric task. The ideas can be
useful in topography and architecture. With this concept you can
measure an angle without the need for a protractor.

Precondition: 
0 < a,b,c ≤ 1000
'''
import unittest
import math

def find_angle(sides):
	x = (sides[0]**2 + sides[1]**2 - sides[2]**2) / (2*sides[0]*sides[1])
	try: return round(math.degrees(math.acos(x)))
	except: return 0

def checkio(a, b, c):
	angles = list(map(find_angle, [(a, b, c), (a, c, b), (b, c, a)]))
	return sorted(angles) if 0 not in angles else [0,0,0]


class Test(unittest.TestCase):
	def test_cases(self):
		assert checkio(1, 1, 2) == [0, 0, 0], "It's can not be a triangle"
		assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
		assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
		assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	unittest.main()

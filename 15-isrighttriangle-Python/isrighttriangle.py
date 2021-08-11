# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

import math

def getDistance(x1, y1, x2, y2):
	return ((x2-x1)**2 + (y2-y1) ** 2) ** 0.5

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	a = getDistance(x1, y1, x2, y2)
	b = getDistance(x2, y2, x3, y3)
	c = getDistance(x1, y1, x3, y3)
	if a > b and a > c:
		return math.isclose(a ** 2, b ** 2 + c ** 2)
	if b > c and b > a:
		return math.isclose(b ** 2, a ** 2 + c ** 2)
	if c > b and c > a:
		return math.isclose(c ** 2, b ** 2 + a ** 2)
	

# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	if x == y:
		return True
	dig_count = 0
	
	temp = x
	while temp > 0:
		dig_count += 1
		temp //= 10
	dig_count_temp = dig_count

	while dig_count_temp > 0:
		rem = x % 10
		x //= 10
		x += rem * 10**(dig_count-1)
		if x == y:
			return True
		dig_count_temp -= 1
		print(x)
	return False 
		
# print(isrotation(12345,54321))
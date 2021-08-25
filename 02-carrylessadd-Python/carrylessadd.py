# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	res = 0
	p = 0
	while x > 0 or y > 0:
		rem1 = x % 10 if x > 0 else 0
		rem2 = y % 10 if y > 0 else 0
		s = x + y if x + y < 10 else (x + y) % 10
		res = (s * 10 ** p) + res
		p += 1
		x //= 10
		y //= 10
	return res


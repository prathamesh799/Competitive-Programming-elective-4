# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def isAutomorphic(n):
	if n == 0:
		return True
	r = n % 10
	if r not in [1, 5, 6]:
		return False
	s = n ** 2
	while n > 0:
		r1 = n % 10
		r2 = s % 10
		if r1 != r2:
			return False
		n //= 10
		s //= 10
	return True

# print([i for i in range(1000) if isAutomorphic(i)])
def nthautomorphicnumbers(n):
	# Your code goes here
	num = 0
	while n > 0:
		if isAutomorphic(num):
			n -= 1
		num += 1
	return num - 1

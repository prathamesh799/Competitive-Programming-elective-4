# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def getDigitCount(n, c):
	if n <= 0:
		return c
	c += 1
	return getDigitCount(n//10, c)

def rev(n, r, dig_cnt):
	if n <= 0:
		return r
	rem = n % 10
	n //= 10
	r += rem * (10 ** (dig_cnt-1))
	return rev(n, r, dig_cnt-1)

def isPalin(n):
	return n == rev(n, 0, getDigitCount(n, 0))

def isLychrel(n, k):
	# gets reverse of number
	while k > 0:
		rev_num = rev(n, 0, getDigitCount(n, 0))
		n = n + rev_num
		if isPalin(n):
			return False
		k -= 1
	return True


def nthlychrelnumbers(n):
	# your code goes here
	num = 196
	k = 50
	while n > 0:
		if isLychrel(num, k):
			n -= 1
		num += 1
	return num - 1

# for i in range(1,10):
# 	print(nthlychrelnumbers(i))
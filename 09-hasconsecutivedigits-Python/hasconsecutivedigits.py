# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n = -n if n < 0 else n
	prev = n % 10
	n //= 10
	while n > 0:
		rem = n % 10
		if rem == prev:
			return True
		prev = rem
		n //= 10
	return False
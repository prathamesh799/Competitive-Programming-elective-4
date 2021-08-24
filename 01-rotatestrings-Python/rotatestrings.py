# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')

def rotateLeft(s, n):
	n = n % len(s)
	while n > 0:
		last = s[-1]
		s = last + s[:-1]
		n -= 1
	return s

def rotateRight(s, n):
	n = n % len(s)
	while n > 0:
		first = s[0]
		s = s[1:] + first
		n -= 1
	return s

def fun_rotatestrings(s, n):
	if n < 0:
		return rotateLeft(s, -n)
	return rotateRight(s, n)

# print(fun_rotatestrings('abcd', -6))
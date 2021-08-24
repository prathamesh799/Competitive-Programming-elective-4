# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

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

def rec_even(n, r):
	if n <= 0:
		return r
	rem = n % 10
	if rem % 2 == 0:
		r = r * 10 + rem
	return rec_even(n//10, r)

def rec_alternating(l, i, res):
	if i == len(l):
		return res
	ans = rec_even(l[i], 0)
	ans_rev = rev(ans, 0, getDigitCount(ans, 0))
	res.append(ans_rev)
	return rec_alternating(l, i+1, res)

def fun_recursion_onlyevendigits(l): 
		return rec_alternating(l, 0, []) # 0 is index, [] is result list
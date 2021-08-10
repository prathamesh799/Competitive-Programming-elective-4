# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def fun_set_kth_digit(n, k, d):
	t = n
	i = k
	rem = 0
	if t < 0:
		t = -t
	while i >= 0:
		rem  = t % 10
		t = t//10
		i -= 1
		print(rem)

	return n + 10**k * (d - rem) if n > 0 else n - 10**k * (d - rem)
	# t = n

# print(fun_set_kth_digit(234, 1, 5)) #254
# print(fun_set_kth_digit(-24434, 3, 9)) #254

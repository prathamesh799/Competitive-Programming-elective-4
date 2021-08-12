# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(n, k):
	n = -n if n < 0 else n
	while k > 0 and n > 0:
		n //= 10
		k -= 1
	return n % 10 if n > 0 else 0

# print(fun_get_kth_digit(234,2)) # 2
# print(fun_get_kth_digit(234,3)) # 0
# print(fun_get_kth_digit(234,0)) # 4
# print(fun_get_kth_digit(-234,3)) # 0
# print(fun_get_kth_digit(-234,1)) # 3
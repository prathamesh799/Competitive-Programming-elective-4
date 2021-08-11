# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	d = {}
	while n > 0:
		rem = n % 10
		d[rem] = d.get(rem, 0) + 1
		n //= 10
	# print(d)
	mc = -1
	md = 0
	for k, v in d.items():
		if v > mc:
			mc = v
			md = k
		elif v == mc:
			md = md if md < k else k
		# print(md)
	return md

print(mostfrequentdigit(26011))
# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def isPrime(n):
	if n < 2:
		return False
	if n == 2 or n == 3:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True

def getFactors(n):
	factors = set()
	for i in range(2,int(n//2)+1):
		if n % i == 0:
			factors.add(i)
	return list(factors)

def getPrimeFactors(n):
	p_factors = []
	f = getFactors(n)
	# print('factors', f)
	for each in f:
		if isPrime(each) == True:
			p_factors.append(each)
	return p_factors

def isPowerful(n):
	# print('n', n)
	if n == 0:
		return 1
	pf = getPrimeFactors(n)
	# print('p factors', pf)
	if len(pf) == 0:
		return False
	isPow = None
	for i in range(len(pf)):
		if n % (pf[i] ** 2) == 0:
			isPow = True
		else:
			isPow = False
			break
	return isPow == True
		

def nthpowerfulnumber(n):
	if n == 0:
		return 1
	num = 1
	while n > 0:
		if isPowerful(num) == True:
			n -= 1
		num += 1
	return num - 1

# for each in [17, 216, 225, 243, 256, 288, 289, 324, 343, 361, 392, 400, 432, 441, 484, 500, 512, 529, 576, 625, 648, 675, 676, 729, 784, 800, 841, 864, 900, 961]:
# 	print(isPowerful(each))
# print(isPowerful(4))
# for num in range(20):
# 	print(nthpowerfulnumber(num))
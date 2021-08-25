# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sq = int(n ** 0.5)
    for i in range(3, sq+1):
        if n % i == 0:
            return False
    return True

def primeFactorize(n):
    pf = []
    num = 2
    while n > 1:
        while n % num == 0:
            pf.append(num)
            n //= num
        num += 1
        while not isPrime(num) and num < n:
            num += 1
    return pf

def digitSum(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

def lisNumsSum(L):
    res = 0
    for each in L:
        res += digitSum(each)
    return res

def isSmith(n):
    p_facs = primeFactorize(n) if not isPrime(n) else [0]
    return lisNumsSum(p_facs) == digitSum(n)

def fun_nth_smithnumber(n):
	num = 4
	while n > -1:
		if isSmith(num):
			n -= 1
		num += 1
	return num - 1

# print(getPrimeFactors(4))
# print(getPrimeFactors(49))
# print(getPrimeFactors(6036))
# print(isPrime(85))
# print(lisNumsSum(primeFactorize(85)))
# print(digitSum(85))
# for i in range(1000):
#     if isSmith(i):
#         print(i)
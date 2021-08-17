# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isHappy(num):
	s = num
	if num == 7:
		return True
	while s > 9:	
		s = 0
		while num > 0:
			s += (num % 10) ** 2
			num //= 10
		num = s
	return s == 1

def isPrime(n):
	if n < 2:
		return False
	if n == 2 or n == 3:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True

def fun_nth_happy_prime(n):
	num = 5
	while n > -1:
		if isPrime(num) == True and isHappy(num) == True:
			n -= 1
		num += 1
	return num - 1

# for i in range(20):
# 	print(fun_nth_happy_prime(i))
# print(fun_nth_happy_prime(1))
# print(isHappy(28))
# print(isHappy(68))
# print(isHappy(236))
# print(isHappy(237))
# print(isHappy(235))
# print(isHappy(69))
# print(isPrime(49))
# print(isPrime(0))
# print(isPrime(3))
# print(isPrime(4))
# print(isHappy(4))
# print(isPrime(7))
# print(isHappy(7))
# print(isPrime(10))
# print(isPrime(99))
# print(isPrime(47))
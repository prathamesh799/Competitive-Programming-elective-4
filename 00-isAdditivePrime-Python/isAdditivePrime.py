# IsAdditivePrime: Additive primes can be defined as prime numbers where the sum of its digits is a prime number. Write a function isAdditivePrime that takes n as an integer and returns True if n is an Additive Prime and False otherwise.
# Some of the Additive Primes are 2, 3, 5, 7, 11, 23, 29, and etc.
# 29 = 2 + 9 = 11 = 1 + 1 = 2 and 2 is a prime number.
# Here are sample test cases:
# assert (isAdditivePrime(2) == True)
# assert (isAdditivePrime(3) == True)
# assert (isAdditivePrime(5) == True)
# assert (isAdditivePrime(13) == False)
# assert (isAdditivePrime(23) == True)
# assert (isAdditivePrime(29) == True)
# assert (isAdditivePrime(41) == True)
# assert (isAdditivePrime(98) == False)
# assert (isAdditivePrime(198) == False)
# assert (isAdditivePrime(290) == False)
# assert (isAdditivePrime(67) == True)
# assert (isAdditivePrime(97) == False)
# print("All test cases passed... :-)")

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

def digitSum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def isAdditivePrime(n):
    return isPrime(n) == True and isPrime(digitSum(n))

assert (isAdditivePrime(2) == True)
assert (isAdditivePrime(3) == True)
assert (isAdditivePrime(5) == True)
assert (isAdditivePrime(13) == False)
assert (isAdditivePrime(23) == True)
assert (isAdditivePrime(29) == True)
assert (isAdditivePrime(41) == True)
assert (isAdditivePrime(98) == False)
assert (isAdditivePrime(198) == False)
assert (isAdditivePrime(290) == False)
assert (isAdditivePrime(67) == True)
assert (isAdditivePrime(97) == False)
print("All test cases passed... :-)")
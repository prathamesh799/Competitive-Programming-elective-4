# comment
# isPalindromicPrime() Write a function isPalindromicPrime that takes a 
# value n as a parameter and returns True if the given n is a palindrome 
# and prime and False otherwise.

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

def getReversed(n):
    s = 0
    while n > 0:
        r = n % 10
        s = s * 10 + r
        n //= 10
    return s

def isPalindrome(n):
    return n == getReversed(n)

def isPalindromicPrime(n):
    return isPrime(n) and isPalindrome(n)

assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")
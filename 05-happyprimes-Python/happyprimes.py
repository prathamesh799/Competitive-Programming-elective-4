# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

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

def ishappyprimenumber(n):
    # Your code goes here
    return isPrime(n) and isHappy(n)
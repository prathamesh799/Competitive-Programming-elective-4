# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def isHappy(num):
	s = num
	if num == 7 or num == 1:
		return True
	while s > 9:	
		s = 0
		while num > 0:
			s += (num % 10) ** 2
			num //= 10
		num = s
	return s == 1

def nth_happy_number(n):
	num = 0
	n -= 1
	while n > -1:
		if isHappy(num) == True:
			n -= 1
		num += 1
	return num - 1

# print(nth_happy_number(1))
# print(nth_happy_number(2))
# print(nth_happy_number(3))


# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

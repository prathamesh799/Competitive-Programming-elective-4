# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def hasProperty309(num):
	d = {k:0 for k in range(10)}
	num = num ** 5
	while num > 0:
		rem = num % 10
		d[rem] = 1
		num //= 10
	return sum(d.values()) == 10

def nthwithproperty309(n):
    num = 308
    while n > -1:
        if hasProperty309(num) == True:
            n -= 1
        num += 1
    return num - 1

# print(417**5)
# print(418**5)
# print(hasProperty309(417))
# print(hasProperty309(462))
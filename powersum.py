# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k) or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a**2, b//2)
    else:
        return a * power(a, b-1)

# print(power(2,4))
# print(power(2,5))

def powerSum(n, k):
    return sum([power(i, k) for i in range(1,n+1)])

# Write your own test cases here...
assert(powerSum(2,10) == 1025)
assert(powerSum(3,10) == 60074)
print ("All test cases passed...")
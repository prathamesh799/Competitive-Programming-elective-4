# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math
def getSplits(n):
    n = str(n)
    res = []
    for i in range(1, len(n)):
        s1 = int(n[:i])
        s2 = int(n[i:])
        # while s1 != 0 and s1 % 10 == 0:
        #     s1 //= 10
        # while s2 != 0 and s2 % 10 == 0:
        #     s2 //= 10
        if s1 == 0 or s2 == 0 or (s1, s2) in res:
            continue
        res.append((s1, s2))
    return res

def isKaprekar(n):
    if n == 1:
        return True
    s = n ** 2
    splits = getSplits(s)
    for each in splits:
        if each[0] + each[1] == n:
            return True
    return False

def fun_nth_kaprekarnumber(n):
    num = 1
    n += 1
    while n > 0:
        if isKaprekar(num):
            n -= 1
        num += 1
    return num - 1

# print(getSplits(2025))
# print(getSplits(1000))
# print(getSplits(1))
# print(isKaprekar(1))
# print(isKaprekar(9))
# print(isKaprekar(45))
# print(isKaprekar(55))
# print(fun_nth_kaprekarnumber(1))
# print([fun_nth_kaprekarnumber(i) for i in range(21)]) 
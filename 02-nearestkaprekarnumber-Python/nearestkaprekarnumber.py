# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.

import math

def getSplits(n):
    n = str(n)
    res = []
    for i in range(1, len(n)):
        s1 = int(n[:i])
        s2 = int(n[i:])
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

def fun_nearestkaprekarnumber(n):
    diff = 1
    while True:
        if isKaprekar(n - diff):
            return n - diff
        elif isKaprekar(n + diff):
            return n + diff
        diff += 1
# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def isTidy(num):
    rem = 10
    while num > 0:
        if num % 10 > rem:
            return False
        rem = num % 10
        num //= 10
    return True

def fun_nth_tidynumber(n):
    num = 1
    while n > -1:
        if isTidy(num):
            n -= 1
        num += 1
    return num - 1
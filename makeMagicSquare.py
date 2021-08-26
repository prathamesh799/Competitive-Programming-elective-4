# makeMagicSquare(n)
# Write the function makeMagicSquare(n) that takes a positive 
# odd integer n and returns an nxn magic square by following 
# the resource here. If n is not a positive odd integer, 
# return None.

# URL: https://en.wikipedia.org/wiki/Magic_square

# Hints: From Geeks for Geeks.
# Did you find any pattern in which the numbers are stored? 

# In any magic square, the first number i.e. 1 is 
# stored at position (n/2, n-1). Let this position 
# be (i,j). The next number is stored at position (i-1, j+1) 
# where we can consider each row & column as circular array 
# i.e. they wrap around.

# Three conditions hold:

# 1. The position of next number is calculated by 
# decrementing row number of the previous number by 1,
#  and incrementing the column number of the previous 
# number by 1. At any time, if the calculated row position 
# becomes -1, it will wrap around to n-1. Similarly, if 
# the calculated column position becomes n, it will wrap 
# around to 0.

# 2. If the magic square already contains a number at the 
# calculated position, calculated column position will be 
# decremented by 2, and calculated row position will be 
# incremented by 1.

# 3. If the calculated row position is -1 & calculated 
# column position is n, the new position would be: (0, n-2). 

def makeMagicSquare(n):
    # Your code goes here...
    res = [[0 for i in range(n)] for j in range(n)]
    i, j = n//2, n-1
    num = 1
    # base condition
    res[i][j] = num
    while num < n*n:
        # condition 1
        num += 1
        i = i-1 if i != 0 else n-1
        j = j+1 if j != n-1 else 0
        # condition 2
        if res[i][j] != 0:
            i += 1
            j -= 2
            # condition 3
            if i == -1 and j == n:
                i = 0
                j = n-2
        i = i % n
        j = j % n
        res[i][j] = num
    return res

print('starting tests...')
assert(makeMagicSquare(3) == [[2, 7, 6], [9, 5, 1], [4, 3, 8]])
assert(makeMagicSquare(4) == [[8, 3, 14, 9], [2, 13, 12, 7], [16, 11, 6, 1], [10, 5, 4, 15]])
assert(makeMagicSquare(5) == [[9, 3, 22, 16, 15], [2, 21, 20, 14, 8], [25, 19, 13, 7, 1], [18, 12, 6, 5, 24], [11, 10, 4, 23, 17]])
print('passed!!')
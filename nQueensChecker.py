# nQueensChecker(a)
# Background: The "N Queens" problem asks if we can place N queens on an NxN
#  chessboard such that no two queens are attacking each other. 
# For most values of N, there are many ways to solve this problem. 
# Here, you will write the function nQueensChecker(board) that takes a 
# 2d list of booleans where True indicates a queen is present and False
#  indicates a blank cell, and returns True if this NxN board contains N
#  queens all of which do not attack any others, and False otherwise.

"""
1. Place a queen col by col
2. check if it's safe to place queen here
    - If there is another queen to left, return False
    - Check left upper diagonal, if present return False
    - Check lower left diagonal, if present return False
3. If safe place queen and check if issafe for col+1
"""
def isSafe(a, row, col):
    n = len(a)
    # condition 2.1
    for j in range(col):
        # print('col=', col, j)
        if [row][j] == 1:
            return False
    
    # condition 2.2
    for x in range(row, -1, -1):
        for y in range(col, -1, -1):
            if a[x][y] == 1:
                return False
    
    # condition 2.3
    for x in range(row, n,1):
        for y in range(col, -1, -1):
            if a[x][y] == 1:
                return False
    return True

def rec_check(a, col):
    n = len(a)
    if col >= n:
        return True
    for i in range(n):
        if isSafe(a, i, col):
            # a[i][col] = 1
            if rec_check(a, col+1) == True:
                return True
            # a[i][col] = 0
    return False


def nQueensChecker(a):
    # Your code goes here...
    return True if rec_check(a, 0) == True else False
    
nq_3 = [[]]
nq_4 = [[0,1,0,0], [0,0,0,1], [1,0,0,0], [0,0,1,0]]
nq_5 = [
   [0, 0, 0, 1, 0],
   [0, 1, 0, 0, 0],
   [0, 0, 0, 0, 1],
   [0, 0, 1, 0, 0],
   [1, 0, 0, 0, 0]
]
# print(nQueensChecker(nq_3))
print(nQueensChecker(nq_4))
print(nQueensChecker(nq_5))
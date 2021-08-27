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
def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	r = qR - oR
	c = qC - oC
	if r == c:
		return True

	elif qR == oR:
		return True

	elif qC == oC:
		return False
		
	return False


def nQueensChecker(a):
    l = []
    for i in range(N):
        for j in range(N):
            if a[i][j] == 1:
                l.append([i,j])
   
    for i in range(len(l)):
        
        for j in range(i+1,len(l)):
            if canqueenattack(l[i][0],l[i][1],l[j][0],l[j][1]) == True:
                return False
    return True
a =[[0,0,1,0],[1,0,0,0],[0,0,0,1],[0,1,0,0]]

N = len(a)
b = [[0]*N for _ in range(N)]
    
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
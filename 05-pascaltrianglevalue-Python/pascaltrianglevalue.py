# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

def buildTriangle(r):
	r += 1
	t = [[0 for i in range(r)] for i in range(r)]
	for i in range(r):
		t[i][0] = 1
	for i in range(1,r):
		for j in range(r):
			t[i][j] = t[i-1][j] + t[i-1][j-1]
	return t

def fun_pascaltrianglevalue(row, col):
	if col > row:
		return 0
	triangle = buildTriangle(row)
	# print(triangle)
	return triangle[row][col]

# print(fun_pascaltrianglevalue(7,7))
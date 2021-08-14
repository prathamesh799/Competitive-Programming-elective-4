# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# sum of rows must be same
	l = len(a)
	rs = sum(a[0])
	for row in range(1, l):
		if sum(a[row]) != rs:
			return False

	# sum of column should be same
	# first loop goes through all column nums
	
	cs = 0
	for i in range(len(a[0])):
		# adds up all rows of i column
		col_vals = [a[k][i] for k in range(l)]
		ps = sum(col_vals)
		if cs == 0:
			cs = ps
		elif cs != ps:
			return False

	# sum of diagonal 1 and diagonal 2 must be same
	# diagonal 1 has (0,0), (1,1), (2,2), (3,3)
	dg1 = [a[i][i] for i in range(l)]

	# diagonal 2 has (0,3), (1,2), (2,1), (3,0)
	dg2 = [a[i][l-i-1] for i in range(len(a))]

	if sum(dg1) != sum(dg2):
		return False
	return True

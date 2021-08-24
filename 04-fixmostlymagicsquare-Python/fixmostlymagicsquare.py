# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.

def fixmostlymagicsquare(a):
	# sum of rows must be same
	l = len(a)
	row_sums = []
	col_sums = []

	not_magic_row = None
	not_magic_col = None

	req_row_sum = None
	req_col_sum = None

	for row in range(l):
		t = sum(a[row])
		row_sums.append(t)

	for s in range(l):
		if row_sums.count(row_sums[s]) == 1:
			not_magic_row = s
		else:
			req_row_sum = row_sums[s]

	# sum of column should be same
	# first loop goes through all column nums
	for i in range(len(a[0])):
		# adds up all rows of i column
		col_vals = [a[k][i] for k in range(l)]
		ps = sum(col_vals)
		col_sums.append(ps)
	
	for c in range(len(a[0])):
		if col_sums.count(col_sums[c]) == 1:
			not_magic_col = c
		else:
			req_col_sum = col_sums[s]	

	if row_sums[not_magic_row] > req_row_sum:
		row_sum_diff = row_sums[not_magic_row] - req_row_sum
		a[not_magic_row][not_magic_col] = a[not_magic_row][not_magic_col] - row_sum_diff
	else:
		row_sum_diff = req_row_sum - row_sums[not_magic_row]
		a[not_magic_row][not_magic_col] = a[not_magic_row][not_magic_col] + row_sum_diff
	return a

# def fixmostlymagicsquare(L):
# 	# Your code goes here
# 	pass

# print(ismostlymagicsquare([[2, 7, 9], [9, 5, 1], [4, 3, 8]]))
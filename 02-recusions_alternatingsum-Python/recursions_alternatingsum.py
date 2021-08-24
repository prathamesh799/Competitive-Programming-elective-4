# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

def rec_alternating(l, i, res):
	if i == len(l):
		return res
	if i % 2 != 0:
		res -= l[i]
	else:
		res += l[i]
	return rec_alternating(l, i+1, res)

def fun_recursions_alternatingsum(l): 
	return rec_alternating(l, 0, 0) # 0 for index, 0 for result sum
# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	l = len(a)
	if l <= 1:
		return True
	if a[0] < a[1]:
		i = 1
		while i < l and a[i] >= a[i-1]:
			i +=1
		if i != l:
			return False
	elif a[0] > a[1]:
		i = 1
		while i < l and a[i] <= a[i-1]:
			i +=1
		if i != l:
			return False
	return True

print(issorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
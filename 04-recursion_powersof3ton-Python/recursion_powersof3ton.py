# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

# def recursion_powersof3ton(n):
# 	# Your code goes here
# 	num = 0
# 	res = []
# 	while 3 ** num <= n:
# 		res.append(3 ** num)
# 		num += 1
# 	return res if len(res) > 0 else None

def rec_ton(n, i, res):
	if 3**i > n:
		return res
	res.append(3**i)
	return rec_ton(n, i+1, res)

def recursion_powersof3ton(n):
	res = rec_ton(n, 0, [])
	return res if len(res) > 0 else None  

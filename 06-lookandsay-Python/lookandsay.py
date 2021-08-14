# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	res = []
	if len(a) == 0:
		return res
	pres = a[0]
	pc = 1
	for i in range(1,len(a)):
		if a[i] != pres:
			res.append((pc, pres))
			pres = a[i]
			pc = 1
		else:
			pc += 1
		# print(pres, pc, res)
	res.append((pc, pres))
	return res

# print(lookandsay([3,3,8,3,3,3,3]))
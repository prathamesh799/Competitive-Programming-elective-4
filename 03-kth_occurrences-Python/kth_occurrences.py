# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.

def fun_kth_occurrences(s, n):
	d = {}
	for ch in s:
		d[ch] = d.get(ch, 0) + 1
	res = []
	for k, v in d.items():
		res.append((k,v))
	# d = sorted(d, key = lambda x:x[1], reverse=True)
	# print(d)
	res = sorted(res, key = lambda x:x[1], reverse=True)
	# print(res)
	return res[n-1][0]

# print(fun_kth_occurrences("helllo woorld", 2))
# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. 
# For example, if given input is "abc" then 
# your program should print all 6 permutations 
# e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

def rec_perm(s, i, l, res):
	if i == l:
		res.append(tuple(s))
	else:
		for j in range(i, l):
			s[i], s[j] = s[j], s[i]
			rec_perm(s, i+1, l, res)
			s[i], s[j] = s[j], s[i]

def getallpermutations(x):
	# Your code goes here
	res = []
	s = list(sorted(x))
	rec_perm(s, 0, len(x), res)
	return sorted(res)

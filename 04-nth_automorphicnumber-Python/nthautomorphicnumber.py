# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def isAutomorphic(n):
	if n == 0:
		return True
	r = n % 10
	if r not in [1, 5, 6]:
		return False
	s = n ** 2
	while n > 0:
		r1 = n % 10
		r2 = s % 10
		if r1 != r2:
			return False
		n //= 10
		s //= 10
	return True

# print([i for i in range(1000) if isAutomorphic(i)])
def nthautomorphicnumbers(n):
	temp = n
	# Your code goes here
	num = 0
	pot = [0,1,5,6]
	if n < 4:
		return pot[n]
	while n > 0:
		# print('pot', pot)
		found = False
		j = 1
		while True:
			found = False
			for i in range(len(pot)):
				t_num = int(str(j) + str(pot[i]))
				if t_num not in pot and isAutomorphic(t_num):
					pot.append(t_num)
					n -= 1
					found = True
				if found == True:
					break
			if found == True:
				break
			j += 1
		pot.sort()
	print(pot)
	return pot[temp]

print(nthautomorphicnumbers(25))
# for i in range(20):
# 	print(nthautomorphicnumbers(i))
# print(isAutomorphic(81787109376))
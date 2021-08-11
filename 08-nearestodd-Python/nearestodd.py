# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	if int(n) % 2 != 0:
		return int(n)
	elif n - float(int(n)) > 0.0: 
		return int(n) + 1
	return int(n) - 1

# print(fun_nearestodd(4.1)) # 5
# print(fun_nearestodd(4.9)) # 5
# print(fun_nearestodd(4.0)) # 3
# print(fun_nearestodd(3.0)) # 3
# print(fun_nearestodd(3.1)) # 3
# print(fun_nearestodd(3.9)) # 3
# print(fun_nearestodd(0)) # 1

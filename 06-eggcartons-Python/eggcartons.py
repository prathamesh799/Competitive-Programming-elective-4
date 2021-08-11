# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	print(eggs)
	if eggs == 0:
		return 0
	elif eggs <= 12:
		return 1
	elif eggs % 12 == 0:
		return eggs // 12
	else:
		return eggs // 12 + 1

print(fun_eggcartons(0)) #0
print(fun_eggcartons(11)) #1
print(fun_eggcartons(12)) #1
print(fun_eggcartons(13)) #2
print(fun_eggcartons(24)) #2
print(fun_eggcartons(25)) #3
print(fun_eggcartons(35)) #3
print(fun_eggcartons(36)) #3
print(fun_eggcartons(37)) #4



# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	bs = street // 8
	rem = street % 8
	if rem > 4:
		return (bs + 1) * 8
	return bs * 8

# print(fun_nearestbusstop(13)) #16
# print(fun_nearestbusstop(17)) #16
# print(fun_nearestbusstop(21)) #24

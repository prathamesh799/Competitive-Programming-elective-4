# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.

def fun_getaverage(s):
	s = s.split(',')
	nums = []
	for each in s:
		for ch in each:
			if ord(ch) > 47 and ord(ch) < 59:
				nums.append(int(each))
			break
	return sum(nums) / len(nums) if len(nums) > 0 else 0.0

# print(fun_getaverage('a,12,c,14,6,0'))
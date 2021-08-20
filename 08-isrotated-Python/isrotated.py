# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.

# O(2N) solution
def getIndex(s2, ch):
	for i in range(len(s2)):
		if s2[i] == ch:
			return i
	return -1

def isrotated(str1, str2):
	i = 0
	j = getIndex(str2, str1[0])
	if j == -1:
		return False
	for i in range(len(str1)):
		if str1[i] != str2[j]:
			return False
		j += 1
		if j == len(str2):
			j = 0
	return True
		

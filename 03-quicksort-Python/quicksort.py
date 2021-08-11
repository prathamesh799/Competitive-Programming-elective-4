"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	# Your code goes here
	l = len(array)
	for i in range(l):
		pivot = array[i]
		l, h = i + 1, l-1
		while l < h:
			while l < i and array[l] <= pivot:
				l += 1
			while h > i and array[h] > pivot:
				h -= 1
			if l < h:
				array[l], array[h] = array[h], array[l]
			# else:
			# 	if l < i:
			# 		array[i], array[l] = array[l], array[i]
			# 	if h > i:
			# 		array[i], array[h] = array[h], array[i]
			l += 1
			h -= 1
			print(pivot, array)
print(quicksort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
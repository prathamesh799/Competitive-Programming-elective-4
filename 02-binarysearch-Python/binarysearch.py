"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(arr, value):
    # Your code goes here
    lo = 0
    hi = len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == value:
            return mid
        elif value > arr[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

test_list = [1,3,9,11,15,19,29]

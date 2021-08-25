# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

def limitedPowerSet(n, k):
    # Your code goes here...
    elems = [i for i in range(1, n+1)]
    s_len = 0
    res = [{}]
    while k > 1:
        for z in range(len(elems)-s_len):
            if k == 1:
                break
            s = set(elems[z:z+s_len+1])
            res.append(s)
            k -= 1
        s_len += 1
    return res

print(limitedPowerSet(5,7))
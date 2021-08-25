# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    # Your code goes here...
    d1, d2 = {}, {}
    for ch in s1.lower():
        d1[ch] = d1.get(ch, 0) + 1
    for ch in s2.lower():
        d2[ch] = d2.get(ch, 0) + 1        
    return d1 == d2
# write your test cases here...
assert(areAnagrams('Aba', 'ABA')==True)
assert(areAnagrams('celebrate', 'treecaleb')==True)
print('cases passed')
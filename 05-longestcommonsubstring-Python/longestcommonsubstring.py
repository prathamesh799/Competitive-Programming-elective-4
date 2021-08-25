# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def lcs(s1, s2, x, y, dp, res, temp):
    # if dp[x][y] != 0:
    #     return dp[x][y]
    if x == 0 or y == 0:
        return res
    if s1[x-1] == s1[y-1]:
        temp = temp + s1[x-1]
        if len(temp) > len(res):
            res = temp
    else:
        lcs(s1, s2, x-1, y, dp, res, temp)
        lcs(s1, s2, x, y-1, dp, res, temp)


def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    x, y = len(s1), len(s2)
    dp = [[0 for i in range(len(s2))] for j in range(len(s1))]
    return lcs(s1, s2, x, y, dp, "", "")

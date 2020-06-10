# date 9/jun/20
# 392. Is Subsequence
# Easy

# 1295

# 195

# Add to List

# Share
# Given a string s and a string t, check if s is subsequence of t.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        for each in s:
            if each in t:
                k = t.index(each)
                t = t[k+1::]
            else:
                return False
                
        return True

# Runtime: 12 ms, faster than 98.99% of Python online submissions for Is Subsequence.
# Memory Usage: 13 MB, less than 78.70% of Python online submissions for Is Subsequence.
# date : 9/jun/20
#  3. Longest Substring Without Repeating Characters
# Medium

# 9071

# 549

# Add to List

# Share
# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        crr = 0
        maxm = 0
        i = 0
        k = 0
        check = []
        
        while (i < len(s) and k < len(s)):
            
            if s[i] not in check:
                check.append(s[i])
                i = i+1
                
            else:
                k = k +1
                i = k
                check = []
                
            crr = len(check)
            maxm = max(crr,maxm)
            
        return maxm

# Runtime: 3632 ms, faster than 7.00% of Python online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13.1 MB, less than 52.26% of Python online submissions for Longest Substring Without Repeating Characters.

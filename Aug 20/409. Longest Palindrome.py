# 409. Longest Palindrome
# Easy

# 1116

# 86

# Add to List

# Share
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        oddcount = 0
        k = Counter(s)
        
        if len(k) == 1:
            return len(s)
        else:
            for i in k.keys():
                if k[i]%2 == 0:
                    count = count + k[i]
                else:
                    oddcount = 1
                    count = count + k[i]-1
       
        return (count+oddcount)
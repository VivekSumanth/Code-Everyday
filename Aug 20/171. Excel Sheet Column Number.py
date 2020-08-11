# 171. Excel Sheet Column Number
# Easy

# 1179

# 165

# Add to List

# Share
# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# Example 1:

# Input: "A"
# Output: 1
# Example 2:

# Input: "AB"
# Output: 28
# Example 3:

# Input: "ZY"
# Output: 701
 

# Constraints:

# 1 <= s.length <= 7
# s consists only of uppercase English letters.
# s is between "A" and "FXSHRXW".

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = dict(zip(string.ascii_uppercase, range(1,27)))
        answer = 0
        for i in range(1,len(s)):
            
            answer = answer + (26**i * k[s[len(s)-i-1]])
        
        return answer + k[s[len(s)-1]]
            
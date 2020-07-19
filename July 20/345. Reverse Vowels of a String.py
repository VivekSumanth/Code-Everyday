# 345. Reverse Vowels of a String
# Easy

# 679

# 1130

# Add to List

# Share
# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input: "hello"
# Output: "holle"
# Example 2:

# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        
        s = list(s)
        k = len(s)-1
        i = 0
        if i == k+1:
            return ""
        
        while(i < k):
            
            if s[i] in vowels and s[k] in vowels:
                
                temp = s[i]
                s[i] = s[k]
                s[k] = temp
                
                k = k - 1
                i = i + 1
            
            elif s[k] not in vowels:
                
                k = k - 1
            
            elif s[i] not in vowels:
                
                i = i + 1
                
        print(s)           
        return ''.join(s)
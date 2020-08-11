# 342. Power of Four
# Easy

# 601

# 225

# Add to List

# Share
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        n = bin(num).replace('0b','')
        
        if n[0] == "1" and n.count("1") == 1 :
            if len(n) % 2 == 1:
                
                return True
        return False 
        
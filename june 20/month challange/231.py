# date:8/jun/20
# 231. Power of Two
# Easy

# 789

# 185

# Add to List

# Share
# Given an integer, write a function to determine if it is a power of two.

# Example 1:

# Input: 1
# Output: true 
# Explanation: 20 = 1
# Example 2:

# Input: 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: 218
# Output: false

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 1
        while(i<=n):
            if i == n:
                return True
            i = i*2
            
# Runtime: 20 ms, faster than 65.96% of Python online submissions for Power of Two.
# Memory Usage: 12.7 MB, less than 51.72% of Python online submissions for Power of Two.

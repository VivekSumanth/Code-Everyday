# date : 11/jun/20
# 326. Power of Three
# Easy

# 483

# 1428

# Add to List

# Share
# Given an integer, write a function to determine if it is a power of three.

# Example 1:

# Input: 27
# Output: true
# Example 2:

# Input: 0
# Output: false
# Example 3:

# Input: 9
# Output: true
# Example 4:

# Input: 45
# Output: false
# Follow up:
# Could you do it without using any loop / recursion?


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        return ((n > 0) and (3**30 % n == 0))


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while(i<n):
            power = 3**i
            if power == n:
                return True
            if power > n:
                break
            i = i+1
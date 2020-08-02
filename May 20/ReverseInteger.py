# date : 18/05/20
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x<0):
            x = -(x)
            x = str(x)
            x = x[::-1]
            x = int(x)
            x = -(x)
            
        else:
            x = str(x)
            x = x[::-1]
            x = int(x)
            
        if(x > 2**31-1 or x < ((-2**31))):
            x = 0
        return x

# Runtime: 16 ms, faster than 90.34% of Python online submissions for Reverse Integer.
# Memory Usage: 12.7 MB, less than 5.38% of Python online submissions for Reverse Integer.

# testcase:
    # 1534236469
    # 0
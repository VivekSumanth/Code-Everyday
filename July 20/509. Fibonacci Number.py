# 509. Fibonacci Number
# Easy

# 612

# 193

# Add to List

# Share
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).

 

# Example 1:

# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        table = dict()
        for i in range(N+1):
            table[i] = None

        def memfib(nums):

            if nums is 0 or nums is 1:
                table[nums] = nums

            if table[nums] is None:
                table[nums] = memfib(nums-1) + memfib(nums-2)

            return table[nums]


        return (memfib(N))

# Runtime: 12 ms, faster than 95.78% of Python online submissions for Fibonacci Number.
# Memory Usage: 12.6 MB, less than 83.47% of Python online submissions for Fibonacci Number.
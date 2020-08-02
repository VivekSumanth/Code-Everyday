# 70. Climbing Stairs
# Easy

# 4526

# 145

# Add to List

# Share
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

#memoization
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [None]*(n+1)
        
        def memfib(nums):
        
            if nums is 0:
                table[nums] = 0
            if nums is 1:
                table[nums] = 1
            if nums is 2:
                table[nums] = 2

            if table[nums] is None:
                table[nums] = memfib(nums-1) + memfib(nums-2)


            return table[nums]
        
        return (memfib(n))

#tabulization
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            array = [None]*(n+1)
            array[0] = 0
            array[1] = 1
            array[2] = 2

            for i in range(3,n+1):
                array[i] = array[i-1] + array[i-2]

            return (array[n])
        
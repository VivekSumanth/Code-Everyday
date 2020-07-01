# date: 20/jun/20
# 1137. N-th Tribonacci Number
# Easy

# 249

# 37

# Add to List

# Share
# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

 

# Example 1:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:

# Input: n = 25
# Output: 1389537
 

# Constraints:

# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def recursion(num):
            
            if num == 0:
                return 0
            
            elif num == 1:
                return 1
            
            elif num == 2:
                return 1
            
            else:
                
                return recursion(num-1) + recursion(num-2) + recursion(num-3)
        
        return (recursion(n))
        
-- fails under recursion need effective way


-- dynamic programming

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = dict()
        
        for i in range(n+1):
            cache[i] = None
            

        def recursion(num):
            
            if num == 0 or num == 1:
                cache[num] = num

            elif num == 2:
                cache[num] = 1

            if cache[num] is None:
                
                cache[num] =  recursion(num-1) + recursion(num-2) + recursion(num-3)
               
            return cache[num]

        return (recursion(n))

Runtime: 16 ms, faster than 76.29% of Python online submissions for N-th Tribonacci Number.
Memory Usage: 12.7 MB, less than 61.54% of Python online submissions for N-th Tribonacci Number.
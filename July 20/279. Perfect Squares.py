# 279. Perfect Squares
# Medium

# 2900

# 182

# Add to List

# Share
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        psqure = []
        ht = dict()
        ht[0] = 0
        
        for i in range(1,n+1):
            if i*i <= n:
                psqure.append(i*i)     

        for i in range(1,n+1):
            ht[i] = n+1

        for each in psqure:
            for k in range(each,n+1):
                ht[k] = min(ht[k-each]+1,ht[k])
 
        return ht[n]
                
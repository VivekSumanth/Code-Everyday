# 441. Arranging Coins
# Easy

# 490

# 656

# Add to List

# Share
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.

# n is a non-negative integer and fits within the range of a 32-bit signed integer.

# Example 1:

# n = 5

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤

# Because the 3rd row is incomplete, we return 2.
# Example 2:

# n = 8

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤

# Because the 4th row is incomplete, we return 3.

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while(i<=n):
            n = n - i
            i = i + 1
            
        return i-1

# Runtime: 644 ms, faster than 48.28% of Python online submissions for Arranging Coins.
# Memory Usage: 12.7 MB, less than 53.57% of Python online submissions for Arranging Coins.


# 322. Coin Change
# Medium

# 4057

# 135

# Add to List

# Share
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ht = dict()
        ht[0] = 0
        for i in range(1,amount+1):
            ht[i] = amount+1
        

        for each in coins:
            for k in range(each,amount+1):
                ht[k] = min(ht[k-each]+1,ht[k])

        if ht[amount] <= amount:
            return ht[amount]
        return -1


# Runtime: 1184 ms, faster than 49.22% of Python online submissions for Coin Change.
# Memory Usage: 14.3 MB, less than 18.71% of Python online submissions for Coin Change.
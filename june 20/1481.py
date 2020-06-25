# date : 24/jun/20
# 1481. Least Number of Unique Integers after K Removals
# Medium

# 112

# 5

# Add to List

# Share
# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

# Example 1:

# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.


class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        hastable = Counter(arr)
        hastable = sorted(hastable.items(), key=lambda x: x[1])
        
        for i in hastable:
            
            if k >= i[1]:
                count = count + 1
                k = k - i[1]
        
        return len(hastable) - count
    

# Runtime: 552 ms, faster than 81.98% of Python online submissions for Least Number of Unique Integers after K Removals.
# Memory Usage: 37.2 MB, less than 100.00% of Python online submissions for Least Number of Unique Integers after K Removals.
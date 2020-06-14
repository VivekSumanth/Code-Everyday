# date:13/jun/20
# 5454. Least Number of Unique Integers after K Removals
# Medium

# 14

# 1

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
 

# Constraints:

# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        sets = set(arr)
        count = []
        counter = 0
        for i in sets:
            p = arr.count(i)
            if p <= k:
                count.append([p,i])
 
        for each in count:
            if each[0] <= k:
                counter = counter+1
                k = k-each[0]  
        
        return len(sets)-counter

Time LIMIT EXCEED
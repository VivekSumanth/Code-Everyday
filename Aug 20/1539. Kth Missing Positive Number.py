# 1539. Kth Missing Positive Number
# Easy

# 128

# 1

# Add to List

# Share
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Find the kth positive integer that is missing from this array.

 

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
# Example 2:

# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

# Constraints:

# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length


class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = 1
        
        while(k):
            if count not in arr:
                k = k - 1
                count = count + 1
            else:
                count = count + 1
                
        return count-1
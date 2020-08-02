# date: 28/05/20
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxm = 0
        sumof = 0
        maxarr = []
        for i in nums:
            sumof = maxm +i
            maxm = max(i,sumof)
            maxarr.append(maxm)
        return max(maxarr)

# Runtime: 68 ms, faster than 61.51% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.7 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.


# Kadane’s Algorithm:  https://www.youtube.com/watch?v=2MmGzdiKR9Y

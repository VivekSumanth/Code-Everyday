# date:04/jun/20
# 169. Majority Element
# Easy


# Add to List

# Share
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numbers = set(nums)
       
        for i in numbers:
            count = nums.count(i)
            if count > len(nums)/2:
                return i

# Runtime: 148 ms, faster than 86.56% of Python online submissions for Majority Element.
# Memory Usage: 14.1 MB, less than 37.29% of Python online submissions for Majority Element.

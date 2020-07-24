# 260. Single Number III
# Medium

# 1564

# 104

# Add to List

# Share
# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

# Example:

# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# Note:

# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        j = -(len(nums))
        count = 0
        
        while(j != 0):
            if nums[j] == nums[j+1] != nums[j+2]:
                nums[j],nums[j+1] = None,None
                count = count + 2
            j = j+1
            
        nums.sort()
        return nums[count:]

        
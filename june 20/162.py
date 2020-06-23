# 162. Find Peak Element
# Medium

# 1666

# 2024

# Add to List

# Share
# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak element is 2, 
#              or index number 5 where the peak element is 6.
# Follow up: Your solution should be in logarithmic complexity.

# Accepted


class Solution(object):
    
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def recursive(nums,left,right):
            
            if len(nums) > 1 and left != right:
                
                mid = (left + right)//2

                
                if nums[mid] < nums[mid-1] :
                    
                    return recursive(nums,left,mid)

                elif nums[mid] < nums[mid+1]:
                    
                    return recursive(nums,mid+1,right)

                else:
                    return mid
            else:
                return nums.index(max(nums))
                
                
        return (recursive(nums,0,len(nums)-1))



# 59 / 59 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 12.8 MB
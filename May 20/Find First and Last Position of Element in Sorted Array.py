# date :21/5/20
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output=[]
        
        for i in range(len(nums)):
            if(nums[i] == target):
                output.append(i)   
        l = len(output)
        if(l==0):
            return [-1,-1]
        elif(l==1):
            return ([output[0],output[0]])
        elif(l==2):
            return output
        else:
            return (output[0],output[l-1])

# Runtime: 88 ms, faster than 65.10% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.2 MB, less than 5.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
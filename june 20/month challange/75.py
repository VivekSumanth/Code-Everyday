# date:11/jun/20
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:

# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        indexarray = [0,0,0]
        countarray = [0]*len(nums)
        temp = nums
        
        
        for i in nums:
            indexarray[i] = indexarray[i]+1

        for i in range(1,3):
            indexarray[i] = indexarray[i-1]+indexarray[i]

        
        for i in nums:
            countarray[indexarray[i]-1] = i
            indexarray[i] = indexarray[i]-1
        
        print(countarray)
        
        for i in range(len(nums)):
            nums[i] = countarray[i]

# Runtime: 36 ms, faster than 9.55% of Python online submissions for Sort Colors.
# Memory Usage: 13 MB, less than 5.05% of Python online submissions for Sort Colors.

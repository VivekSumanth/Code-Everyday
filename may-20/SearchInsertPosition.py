# date : 21/05/20
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 4:

# Input: [1,3,5,6], 0
# Output: 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """index_of_nums = 0"""
        def check(nums):
            for i in nums:
                if i == target:
                    flag = True
                    index_of_num = nums.index(i)
                    print (index_of_num)
                    return index_of_num
            else:
                print ('no value found')
                nums.append(target)
                nums.sort()
                print(nums)
                return check(nums)
        lists = check(nums)
        print(lists)
        return lists 
        
# Runtime: 36 ms, faster than 71.74% of Python online submissions for Search Insert Position.
# Memory Usage: 13.2 MB, less than 5.26% of Python online submissions for Search Insert Position.
# 137. Single Number II
# Medium

# 1669

# 335

# Add to List

# Share
# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,3,2]
# Output: 3
# Example 2:

# Input: [0,1,0,1,0,1,99]
# Output: 99

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in nums:
            print(i)
            if nums.count(i) == 1:
                return i

# Runtime: 1192 ms, faster than 6.67% of Python online submissions for Single Number II.
# Memory Usage: 14.3 MB, less than 53.89% of Python online submissions for Single Number II.

# hash table implementation

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashtable = dict()
        
        for i in range(len(nums)):
            
            if nums[i] in hashtable.keys():
                hashtable[nums[i]] += 1
            
            else:
                hashtable[nums[i]] = 1
        
        for i in hashtable :
            
            if hashtable[i] == 1 :
                
                return i

# Runtime: 2260 ms, faster than 5.14% of Python online submissions for Single Number II.
# Memory Usage: 15.1 MB, less than 20.29% of Python online submissions for Single Number II.
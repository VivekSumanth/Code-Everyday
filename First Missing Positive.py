# date:26/05/20
# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        missing = []
        p = 0
        leng = (len(nums)+1)
        for i in range(1,leng):
            if i not in nums:
                missing.append(i)
                print(missing)
            p = i
        if(len(missing) == 0):
            return p+1
        else:
            return missing[0]

# Runtime: 32 ms, faster than 15.57% of Python online submissions for First Missing Positive.
# Memory Usage: 12.8 MB, less than 5.88% of Python online submissions for First Missing Positive.
        
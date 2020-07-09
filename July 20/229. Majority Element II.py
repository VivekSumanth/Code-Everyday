# 229. Majority Element II
# Medium

# 1538

# 167

# Add to List

# Share
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3,2,3]
# Output: [3]
# Example 2:

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# Accepted
# 141,455
# Submissions
# 401,047

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = Counter(nums)
        result = []
        x = sorted(k.items(), key=lambda k: k[1], reverse = True)
        
        for i in x:
            if i[1] > len(nums)/3:
                result.append(i[0])
        
        return result
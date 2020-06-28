# date: 27/jun/20
# 1493. Longest Subarray of 1's After Deleting One Element
# Medium

# 71

# 2

# Add to List

# Share
# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array.

# Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
# Example 4:

# Input: nums = [1,1,0,0,1,1,1,0,1]
# Output: 4
# Example 5:

# Input: nums = [0,0,0]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        al = []
        maxall = 0
        k = ''
        min0 = 1
        i = 0
        count = 0
        
        while(i< len(nums)):

            if nums[i] == 0 and min0 == 1:
                k = k + str(nums[i])
                min0 = min0 - 1
                
            elif nums[i] == 1:
                k = k + str(nums[i])
            
            else:

                al.append(int(k))
                i = count
                count = count + 1
                min0 = 1
                k = ''  

            i = i + 1
        

        if len(al) > 0:
            if max(al) > int(k):
                return (str(max(al))).count('1')
            else:
                return (str(k)).count('1')
        else:
            return len(nums) - 1 

TLE
            
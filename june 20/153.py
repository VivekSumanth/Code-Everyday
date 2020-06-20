# 153. Find Minimum in Rotated Sorted Array
# Medium

# 1991

# 227

# Add to List

# Share
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def merge_sort(values): 

            if len(values)>1: 
                m = len(values)//2
                left = values[:m] 
                right = values[m:] 

                left = merge_sort(left)
                right = merge_sort(right) 

                values = []

                while(len(left)>0 and len(right)>0):
                    if left[0] < right[0]:
                        values.append(left[0])
                        left.pop(0)
                    else:
                        values.append(right[0])
                        right.pop(0)

                for i in left:
                    values.append(i)

                for j in right:
                    values.append(j)

            return values 

        return(merge_sort(nums)[0])

Runtime: 52 ms, faster than 5.24% of Python online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 13.2 MB, less than 5.98% of Python online submissions for Find Minimum in Rotated Sorted Array.
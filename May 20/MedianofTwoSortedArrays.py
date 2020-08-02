# date : 20/05/20
# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = nums1 + nums2
        total.sort()
        k = len(total)
        if(k%2==0):
            return (total[int(k/2)]+total[int(k/2)-1])/2
        else:
            return total[floor(k/2)]


# Runtime: 92 ms, faster than 81.38% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.1 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.
            
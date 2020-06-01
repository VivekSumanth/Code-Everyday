# date: jun/01/20
# 74. Search a 2D Matrix
# Medium

# 1613

# 154

# Add to List

# Share
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false


# binary search implementation

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        def search(matrix,target):
            k = len(matrix)
            if(k ==0):
                return False
            
            mid = int(round(k/2))
            
            if(target in matrix[mid]):
                return True
            
            elif(mid and target < min(matrix[mid])):
                return search(matrix[:mid:],target)

            elif(mid and target > max(matrix[mid]) ):
                return search(matrix[mid+1::],target)
            
            else:
                return False
 
        if(search(matrix,target) == True):
            return True

# Runtime: 52 ms, faster than 71.16% of Python online submissions for Search a 2D Matrix.
# Memory Usage: 14.4 MB, less than 7.14% of Python online submissions for Search a 2D Matrix.

# greedy approach

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            for j in i:
                if j == target:
                    return True
                    break
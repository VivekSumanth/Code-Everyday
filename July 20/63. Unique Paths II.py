# 63. Unique Paths II
# Medium

# 1701

# 237

# Add to List

# Share
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?



# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# Note: m and n will be at most 100.

# Example 1:

# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        mat = [[0 for i in range(col)] for j in range(row)]
        
        mat[0][0] = 1-grid[0][0]
        
        for j in range(1,row):
            mat[j][0] = mat[j-1][0] *(1-grid[j][0])
            
        for i in range(1,col):
            mat[0][i] = mat[0][i-1] *(1-grid[0][i])
            

        for i in range(1,row):
            for j in range(1,col):
                
                    mat[i][j] = (mat[i-1][j] + mat[i][j-1]) * (1 - grid[i][j])

        return mat[-1][-1]
    

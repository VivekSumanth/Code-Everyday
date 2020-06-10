# date: 10/jun/20
# 637. Average of Levels in Binary Tree
# Easy

# 1188

# 163

# Add to List

# Share
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        if root == None:
            return []
       
        q = []
        q.append(root)
        avgv = []
        
        while(len(q)):
            dummy = []
            
            for i in range(len(q)):
                
                temp = q.pop(0)
                
                if temp.left:
                    q.append(temp.left)
                
                if temp.right:
                    q.append(temp.right)
        
                dummy.append(temp.val)
            
            avgv.append((sum(dummy)/float(len(dummy))))

        return avgv

# Runtime: 56 ms, faster than 21.37% of Python online submissions for Average of Levels in Binary Tree.
# Memory Usage: 17.6 MB, less than 31.55% of Python online submissions for Average of Levels in Binary Tree.

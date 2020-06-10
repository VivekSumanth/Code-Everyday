# date 10/jun/20
# 513. Find Bottom Left Tree Value
# Medium

# 849

# 137

# Add to List

# Share
# Given a binary tree, find the leftmost value in the last row of the tree.

# Example 1:
# Input:

#     2
#    / \
#   1   3

# Output:
# 1
# Example 2:
# Input:

#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7

# Output:
# 7

# Note: You may assume the tree (i.e., the given root node) is not NULL.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [root]

        while(len(q)):
            dummy = []
            for i in range(len(q)):
                temp = q.pop(0)
                
                if temp.left:
                    q.append(temp.left)
                
                if temp.right:
                    q.append(temp.right)
                
                dummy.append(temp.val)

        return dummy[0]
        
# Runtime: 64 ms, faster than 5.83% of Python online submissions for Find Bottom Left Tree Value.
# Memory Usage: 17.4 MB, less than 51.48% of Python online submissions for Find Bottom Left Tree Value.

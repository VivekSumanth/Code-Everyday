# date 2/jun/20
# 104. Maximum Depth of Binary Tree
# Easy


# Add to List

# Share
# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if(root == None):
            return 0
        else:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
       
        
        if ldepth > rdepth:
            return ldepth+1
        else:
            return rdepth+1

            
# Runtime: 36 ms, faster than 36.35% of Python online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.5 MB, less than 6.17% of Python online submissions for Maximum Depth of Binary Tree.
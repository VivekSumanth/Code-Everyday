# date : 8/jun/20
# 112. Path Sum
# Easy

# 1759

# 477

# Add to List

# Share
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        
        value = sum - root.val
        flag = set()
        
        def pathsum(root,sum,value):
            if root:
                if value == 0 and root.left == None and root.right == None:
                    flag.add(True)
                    return True
                
                if root.left:
                    pathsum(root.left,sum,value-root.left.val)
                if root.right:
                    pathsum(root.right,sum,value-root.right.val)
        
        pathsum(root,sum,value)
        if True in flag:
            return True
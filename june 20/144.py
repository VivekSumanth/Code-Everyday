# date:4/jun/20
# 144. Binary Tree Preorder Traversal
# Medium


# Add to List

# Share
# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
               
        #recursive
        lis = []
        def preorder(root):
            
            if (root!= None):
                lis.append(root.val)
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)
        return lis
        
# date:14/jun/20
# 98. Validate Binary Search Tree
# Medium

# 3692

# 522

# Add to List

# Share
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# Accepted
# 672,731
# Submissions
# 2,442,195

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, l = None ,r = None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root:
            
            if l:
                if l.val >= root.val:
                    return False
            if r:
                if r.val <= root.val:
                    return False
                
        return self.isValidBST(root.left,l,root) and self.isValidBST(root.right,root,r)

# Runtime: 32 ms, faster than 87.83% of Python online submissions for Validate Binary Search Tree.
# Memory Usage: 17.4 MB, less than 63.54% of Python online submissions for Validate Binary Search Tree.
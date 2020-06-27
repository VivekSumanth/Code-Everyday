# date: 26/jun/20
# 110. Balanced Binary Tree
# Easy

# 2166

# 165

# Add to List

# Share
# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

# Example 1:

# Given the following tree [3,9,20,null,null,15,7]:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.

# Example 2:

# Given the following tree [1,2,2,3,3,null,null,4,4]:

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.isbalanced = True
        
        def depth(node): 
            
            if node is None: 
                return 0 ;  

            else : 

                lDepth = depth(node.left) 
                rDepth = depth(node.right) 
                
                if lDepth != None and rDepth != None:
                    if abs(lDepth - rDepth) >= 2:
                        self.isbalanced = False

                if (lDepth > rDepth): 
                    return lDepth+1
                else: 
                    return rDepth+1
               
        depth(root)
        return (self.isbalanced)

# Runtime: 40 ms, faster than 83.27% of Python online submissions for Balanced Binary Tree.
# Memory Usage: 18.4 MB, less than 6.37% of Python online submissions for Balanced Binary Tree.
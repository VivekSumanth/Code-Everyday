# date:24/jun/20
# 543. Diameter of Binary Tree
# Easy

# 2933

# 189

# Add to List

# Share
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        
        def recursion(root):
            
            if root == None:
                return 0

            if root:

                ldepth = recursion(root.left)
                rdepth = recursion(root.right)
               
                self.result = max(self.result,rdepth + ldepth)
                print(root.val,ldepth+rdepth,self.result)
                return max(ldepth,rdepth) + 1
                
        (recursion(root))
        return self.result

# Runtime: 36 ms, faster than 62.31% of Python online submissions for Diameter of Binary Tree.
# Memory Usage: 15.6 MB, less than 71.63% of Python online submissions for Diameter of Binary Tree.


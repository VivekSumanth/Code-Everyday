# date:25/jun/20
# 687. Longest Univalue Path
# Easy

# 1615

# 450

# Add to List

# Share
# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

# The length of path between two nodes is represented by the number of edges between them.

 

# Example 1:

# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2

 

# Example 2:

# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2

 

# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.edges = 0
        
        def nodecount(root):
            if root == None:
                return 0
            
            if root :
                        
                lsim = nodecount(root.left)
                rsim = nodecount(root.right)
                
                if root.left and root.left.val == root.val:
                    lsim = (lsim + 1)
                else:
                    lsim = 0
                    
                if root.right and root.right.val == root.val:
                    rsim = (rsim + 1)
                else:
                    rsim = 0
                
                print(root.val,lsim+rsim)
                self.edges = max(self.edges,lsim + rsim)
                
            return max(lsim,rsim)
        
        nodecount(root)
        return self.edges
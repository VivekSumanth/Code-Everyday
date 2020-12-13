# 404. Sum of Left Leaves
# Easy

# 1358

# 138

# Add to List

# Share
# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
# Accepted
# 202,640
# Submissions
# 391,533

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sums = 0
        
        def leftnode(root,isleft):
            if root != None:
                if isleft == True and root.right == None and root.left == None:
                    self.sums = self.sums + root.val
                leftnode(root.left,True)
                leftnode(root.right,False)
            else:
                return 0
            return self.sums   
                
        return leftnode(root,False)
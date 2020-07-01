# date: 29/jun/20

# 113. Path Sum II
# Medium

# 1712

# 63

# Add to List

# Share
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.sets = []
        self.cur = []
        
        if root == None:
            return None
        
        def recursion(root,tar,path):

            if root:
                
                if root.left == None and root.right == None and root.val == tar:
                     
                    self.cur.append(path.split(','))

                if root.left:
                    
                    recursion(root.left ,  tar - root.val , path + ',' + str(root.left.val))
                    
                if root.right: 
                    
                    recursion(root.right , tar - root.val , path + ',' + str(root.right.val))
                
        recursion(root,sum,str(root.val))

        return (self.cur)
        
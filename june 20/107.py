# date: 10/jun/20
# 107. Binary Tree Level Order Traversal II
# Easy

# 1237

# 206

# Add to List

# Share
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = []
        lis = []
        q.append(root)
        
        while(len(q)):
            dummy = []
            
            for i in range(len(q)):
                temp = q.pop(0)
                
                if temp.left :
                    q.append(temp.left)
                
                if temp.right:
                    q.append(temp.right)
                    
                dummy.append(temp.val)
            
            lis.append(dummy)
            
        lis = lis[::-1]
        return lis

# Runtime: 20 ms, faster than 87.69% of Python online submissions for Binary Tree Level Order Traversal II.
# Memory Usage: 13.1 MB, less than 98.57% of Python online submissions for Binary Tree Level Order Traversal II.
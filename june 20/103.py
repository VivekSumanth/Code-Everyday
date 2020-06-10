# date:10/jun/20
# 103. Binary Tree Zigzag Level Order Traversal
# Medium

# 1885

# 98

# Add to List

# Share
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        print(root)
        if root == None:
            return []
        q = []
        q.append(root)
        lis = []
        k = 0
        while(len(q)):
            dummy = []
            k = k + 1
            for i in range(len(q)): 
                temp = q.pop(0)
                if temp:
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                    dummy.append(temp.val)
            if k%2 == 0:
                dummy = dummy[::-1]
            lis.append(dummy)

        return lis

# Runtime: 40 ms, faster than 6.66% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 13.2 MB, less than 16.33% of Python online submissions for Binary Tree Zigzag Level Order Traversal.

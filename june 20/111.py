# date:10/jun/20
# 111. Minimum Depth of Binary Tree
# Easy

# 1288

# 667

# Add to List

# Share
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []
        minm = 1
        if root == None:
            return 0
        q.append(root)
        while(len(q)):  
            for i in range(len(q)):
                temp = q.pop(0)
                print(minm)
                print(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                if temp.right == None and temp.left == None:
                    return minm
            minm = minm+1

# Runtime: 36 ms, faster than 56.21% of Python online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 15.6 MB, less than 71.76% of Python online submissions for Minimum Depth of Binary Tree.
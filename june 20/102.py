# date:5/jun/20
# 102. Binary Tree Level Order Traversal
# Medium


# Add to List

# Share
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        master = []
        if root == None:
            return []
        
        q.append(root)
        
        while(q):
            cur = []    
            
            for i in range(len(q)):
                temp = q[0]
                q.pop(0)
                if temp.left != None:
                    q.append(temp.left)
                    
                if temp.right != None:
                    q.append(temp.right)
                    
                cur.append(temp.val)
            master.append(cur)
        
        return master 

# Runtime: 16 ms, faster than 97.40% of Python online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13.1 MB, less than 92.80% of Python online submissions for Binary Tree Level Order Traversal.
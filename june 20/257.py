# date:15/jun/20
# 257. Binary Tree Paths
# Easy

# 1599

# 97

# Add to List

# Share
# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        values = []
        temp = ""
        
        def answer(root,values,temp):
            if root:
                temp = temp + str(root.val)
                if root.left == None and root.right == None:
                    values.append(temp)
                    
                answer(root.left,values,temp+'->')
                answer(root.right,values,temp+'->')
        
        answer(root,values,temp)
        return(values)

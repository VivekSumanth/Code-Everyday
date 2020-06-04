# date:4/jun/20
# 94. Binary Tree Inorder Traversal
# Medium



# Add to List

# Share
# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# iterative

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = []
        lis = []
        current  = root 
        
        while True:
            if current != None:
                cur.append(current)
                current = current.left
                
            elif(cur):
                current = cur.pop()
                lis.append(current.val)
                current = current.right
            else:
                break
        return (lis)   
                
# Runtime: 16 ms, faster than 82.91% of Python online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 12.6 MB, less than 83.33% of Python online submissions for Binary Tree Inorder Traversal.

#recursive

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
     
        #recursive
        lis = []
        def inorder(root):
            if(root!=None):
                inorder(root.left)
                lis.append(root.val)
                inorder(root.right)
        
        inorder(root)
        
        return lis

# Runtime: 16 ms, faster than 82.91% of Python online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 12.8 MB, less than 14.81% of Python online submissions for Binary Tree Inorder Traversal.
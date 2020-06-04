# date: jun/02/20
#  101. Symmetric Tree


# Add to List

# Share
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        values=[]
        def ismirror(root1,root2):
            if root1 == None and root2 == None:
                return True
            
            if root1 and root2:
                if root1.val == root2.val:
                    print(root1.val)
                    print(root2.val)
                    
                    return (ismirror(root1.left,root2.right) and ismirror(root1.right,root2.left))

            return False
             
        if ismirror(root,root) != False:
            return True
        else:
            return False


# Runtime: 20 ms, faster than 84.54% of Python online submissions for Symmetric Tree.
# Memory Usage: 13 MB, less than 6.52% of Python online submissions for Symmetric Tree.
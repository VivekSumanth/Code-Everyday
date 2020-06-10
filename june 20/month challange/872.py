# date 9/06/20
# 872. Leaf-Similar Trees
# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

# Constraints:

# Both of the given trees will have between 1 and 200 nodes.
# Both of the given trees will have values between 0 and 200

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        tl1 = []
        tl2 = []
        def tree1(root1):
            
            if root1:
                
                if root1.left == None and root1.right == None:
                    tl1.append(root1.val)

                if root1.left:
                    tree1(root1.left)
                    
                if root1.right:
                    tree1(root1.right)
                    
        def tree2(root2):
            if root2:
                
                if root2.left == None and root2.right == None:
                    tl2.append(root2.val)

                if root2.left:
                    tree2(root2.left)
                    
                if root2.right:
                    tree2(root2.right)
                    
        tree1(root1)
        tree2(root2)
        
        if tl1 == tl2:
            return True

# Runtime: 28 ms, faster than 13.63% of Python online submissions for Leaf-Similar Trees.
# Memory Usage: 12.9 MB, less than 25.16% of Python online submissions for Leaf-Similar Trees.
# date: 26/jun/20
#  129. Sum Root to Leaf Numbers
# Medium

# 1415

# 41

# Add to List

# Share
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# Note: A leaf is a node with no children.

# Example:

# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:

# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.addlist = []
        self.k = ''
        self.count = 0
        def number(root):
            if root == None:
                return 0
            
            if root:
                self.k = self.k + str(root.val)
                ldepth = number(root.left)
                rdepth = number(root.right)
                

                if root.left == None and root.right == None:
                    self.count = self.count + 1
                    print(self.k)
                    self.addlist.append(int(self.k))
                    self.k = self.k[:-self.count]  
                    

        number(root)
        return sum(self.addlist)



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.addlist = []
        self.k = ''
        self.res = 0
        
        def number(root,value):
            if root == None:
                return 0
            
            if root:

                ldepth = number(root.left ,value *10 + root.val)
                rdepth = number(root.right,value *10 + root.val)

                if root.left == None and root.right == None:
                    self.res += value*10 + root.val

        number(root,0)
        return self.res
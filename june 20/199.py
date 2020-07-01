# 199. Binary Tree Right Side View
# Medium

# 2157

# 130

# Add to List

# Share
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# Accepted
# 283,048
# Submissions
# 529,465

                # Queue implementation - FIFO 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        result = [root.val]
        q = [root]
        
        while(len(q)):
            
            cur = []
            
            for i in range(len(q)):
                
                temp = q.pop(0)
                if temp.left:
                    cur.append(temp.left.val)
                    q.append(temp.left)
                if temp.right:
                    cur.append(temp.right.val)
                    q.append(temp.right)

            if len(cur) > 0:
                result.append(cur[-1])
                
        return result

# Runtime: 24 ms, faster than 42.31% of Python online submissions for Binary Tree Right Side View.
# Memory Usage: 12.6 MB, less than 91.75% of Python online submissions for Binary Tree Right Side View.
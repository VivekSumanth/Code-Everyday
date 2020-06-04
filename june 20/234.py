# date :03/jun/20
# 234. Palindrome Linked List
# Easy



# Add to List

# Share
# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        p = []
        while(temp):
            p.append(temp.val)
            temp = temp.next
        
        if p == p[::-1]:
            return True

# Runtime: 76 ms, faster than 50.83% of Python online submissions for Palindrome Linked List.
# Memory Usage: 32 MB, less than 6.90% of Python online submissions for Palindrome Linked List.
# date:12/06/20
# 19. Remove Nth Node From End of List
# Medium

# 3137

# 229

# Add to List

# Share
# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?

# Accepted

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        temp = head
        
        for i in range(n):
            fast = fast.next 
         
        if fast == None:
            return head.next

        while(fast.next):
             temp = temp.next
             fast = fast.next

        temp.next = temp.next.next
        
        return head

# Runtime: 16 ms, faster than 93.94% of Python online submissions for Remove Nth Node From End of List.
# Memory Usage: 12.7 MB, less than 85.40% of Python online submissions for Remove Nth Node From End of List.
# date: 11/jun/20
# 206. Reverse Linked List
# Easy

# 4277

# 87

# Add to List

# Share
# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Accepted


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head        
        prev = None
        while(temp):
            forward = temp.next
            temp.next = prev
            prev = temp
            temp = forward
        return prev
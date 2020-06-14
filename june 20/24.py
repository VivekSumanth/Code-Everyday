# date: 13/jun/20
# 24. Swap Nodes in Pairs
# Medium

# 2150

# 166

# Add to List

# Share
# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

 

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        temp1 = head
        temp2 = head.next
        while(temp2 and temp1):

            x = temp1.val
            temp1.val = temp2.val
            temp2.val = x
            temp1 = temp1.next.next
            
            if temp2.next!= None:
                temp2 = temp2.next.next
            
        return head
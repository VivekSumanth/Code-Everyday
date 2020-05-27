# date:26/05/20
# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        every = []
        dummy = ll = ListNode(0)

        while(head):
            if(head.val != val ):
                every.append(head.val)
            head = head.next

        
        for i in every:
            dummy.next = ListNode(i)
            dummy = dummy.next

        return ll.next

# Runtime: 84 ms, faster than 16.05% of Python online submissions for Remove Linked List Elements.
# Memory Usage: 23 MB, less than 6.90% of Python online submissions for Remove Linked List Elements.
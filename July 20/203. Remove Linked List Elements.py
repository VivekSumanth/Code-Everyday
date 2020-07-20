# 203. Remove Linked List Elements
# Easy

# 1734

# 94

# Add to List

# Share
# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# Accepted
# 351,319
# Submissions
# 915,863

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
        dummy = ListNode(-1)
        dummy.next = head

        dummyx = dummy
        
        while(dummyx.next):
            
            if dummyx.next.val == val:
                dummyx.next = dummyx.next.next
            else:
                dummyx = dummyx.next
        
        return dummy.next
# date:23/05/20
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        temp2 = head
        value = []
        dummy = l1 = ListNode(0)
        
        while(temp):
            if(temp.val not in value ):
                value.append(temp.val)
            temp = temp.next
        print(value)
        
        print(l1)
        for i in value:
            l1.next = ListNode(i)
            l1 = l1.next
        print(dummy.next)
        return dummy.next
        
# Runtime: 120 ms, faster than 5.16% of Python online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 13.3 MB, less than 7.14% of Python online submissions for Remove Duplicates from Sorted List.
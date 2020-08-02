# date: 25/5/20

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll1 = []
        sortedlist = dummy = ListNode(0)
        temp = l1
        temp2 = l2

        while(temp):
            ll1.append(temp.val)
            temp = temp.next
        
        while(temp2):
            ll1.append(temp2.val)
            temp2 = temp2.next
        
        ll1.sort()
        
        for i in ll1:
            dummy.next = ListNode(i)
            dummy = dummy.next
            
        return sortedlist.next

# Runtime: 28 ms, faster than 56.22% of Python online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.6 MB, less than 5.75% of Python online submissions for Merge Two Sorted Lists.
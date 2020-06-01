# date: 25/5/20
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        p = []
        listvalues=[]
        v = 0
        newlist = dummy = ListNode(0)
        
        for i in range(k):
            p.append(i)
            p[i]=(lists[i])
            while(p[i]):
                listvalues.append(p[i].val)
                p[i] = p[i].next
                
        listvalues.sort()
        for each in listvalues:
            dummy.next = ListNode(each)
            dummy = dummy.next
        
        return newlist.next

# Runtime: 84 ms, faster than 96.49% of Python online submissions for Merge k Sorted Lists.
# Memory Usage: 21.5 MB, less than 9.09% of Python online submissions for Merge k Sorted Lists.
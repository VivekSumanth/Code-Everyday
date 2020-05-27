# date: 26/05/20
# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ll = []
        temp = head
        dummy = result = ListNode(0)
        
        while(temp):
            ll.append(temp.val)
            temp = temp.next
        print(ll)
        ll.sort()
        
        for i in ll:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return result.next

# Runtime: 124 ms, faster than 91.99% of Python online submissions for Sort List.
# Memory Usage: 40.3 MB, less than 15.38% of Python online submissions for Sort List.
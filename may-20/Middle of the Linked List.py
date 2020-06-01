# date: 22/05/20
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Note:

# The number of nodes in the given list will be between 1 and 100.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 1 
        temp = head
        
        """length of linkedlist """
        while(temp):
            i = i+1
            temp = temp.next

        divide = ceil(i/2)

        if(i%2 == 0):
            v = 1
        else:
            v = 0
            
        while(v<divide):
            head = head.next
            v = v+1
        return head

# Runtime: 20 ms, faster than 37.70% of Python online submissions for Middle of the Linked List.
# Memory Usage: 12.7 MB, less than 6.25% of Python online submissions for Middle of the Linked List.

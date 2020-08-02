# date: 22/05/20
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

 

# Example 1:


# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:

# Input: head = [0]
# Output: 0
# Example 3:

# Input: head = [1]
# Output: 1
# Example 4:

# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880
# Example 5:

# Input: head = [0,0]
# Output: 0
 

# Constraints:

# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        value = 0
        i = -1
        temp = head
        temp2 = head
        
        '''length of linked list'''
        while(temp):
            i = i+1
            temp = temp.next
        print(i)
        
        '''binary to integer conversion'''
        while(temp2):
            print(temp2.val)
            k = 2**i
            value = value + k*(temp2.val)
            i = i-1
            print(value)
            temp2 = temp2.next
        return value

# Runtime: 16 ms, faster than 85.86% of Python online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 12.6 MB, less than 100.00% of Python online submissions for Convert Binary Number in a Linked List to Integer.
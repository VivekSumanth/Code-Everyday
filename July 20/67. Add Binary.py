# 67. Add Binary
# Easy

# 1787

# 275

# Add to List

# Share
# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.

class Solution(object):
    def addBinary(self, a1, a2):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        leng = max(len(a1),len(a2))
        a1 = a1.zfill(leng)
        a2 = a2.zfill(leng)

        added = ''
        carry = 0

        for i in range(leng-1,-1,-1):
            
            k = int(a1[i])+int(a2[i]) + carry
            
            if k <= 1:
                added = str(k) + added
                carry = 0
            else:
                carry = 1
                
                if k > 2: 
                    added =  '1' + added 
                else:
                    added =  '0' + added

        if carry:
            return (str(carry)+added)   
        return (added)


# 20. Valid Parentheses
# Easy

# 4943

# 216

# Add to List

# Share
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

#  LIFO - everything which comes first should leave Last
#  "{[]}" - { comes first should leave last [ comes ] leaves then } 
# "() [] {}" ( comes and ) closes it [ comes and ] closes it { comes and } closes it  

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hastable = {'}':'{',')':'(',']':'['}
        stack = []
        for i in s:
            
            if i in hastable.values():
                stack.append(i)
            elif i in hastable.keys():
                if stack == [] or hastable[i] != stack.pop():
                    return False
            else:
                return False

        if stack == []:
            return True
                
                
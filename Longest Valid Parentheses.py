# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = list(s)
        print(s)
        k = len(s)
        for i in range(len(s)):
            print(i)
            if(s[i] == "("):
                j = i+1
                while(j<len(s)):
                    if(s[j] == ")"):
                        s[j] = 'x'
                        count = count +1
                        break
                    j = j+1
        print(s)            
        print(count)
        return count


"()(()"
Output:
4
Expected:
2

# wrong testcase

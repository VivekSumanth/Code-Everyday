# 1513. Number of Substrings With Only 1s
# Medium

# 78

# 0

# Add to List

# Share
# Given a binary string s (a string consisting only of '0' and '1's).

# Return the number of substrings with all characters 1's.

# Since the answer may be too large, return it modulo 10^9 + 7.

 

# Example 1:

# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.
# Example 2:

# Input: s = "101"
# Output: 2
# Explanation: Substring "1" is shown 2 times in s.
# Example 3:

# Input: s = "111111"
# Output: 21
# Explanation: Each substring contains only 1's characters.
# Example 4:

# Input: s = "000"
# Output: 0
 

# Constraints:

# s[i] == '0' or s[i] == '1'
# 1 <= s.length <= 10^5

# mathematical approach
class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = s.split('0')
        count = 0
        
        for i in k:
            count = count+(len(i)*(len(i)+1))/2

        return (count) % (10**9 + 7)


#  naive apporoach
class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count = 0
        place = 0
        leng = len(s)

        for i in range(1,leng+1):
            
            z = s[place:i]

            if '0' in z:
                place = place+1

            elif '0' not in z:
                l = len(z)
                for i in range(leng):
                    if z == s[i:i+l]:
                        count = count + 1
                        
        return (count)
        
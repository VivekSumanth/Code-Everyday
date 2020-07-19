# 461. Hamming Distance
# Easy

# 1840

# 160

# Add to List

# Share
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.
# Accepted
# 348,636
# Submissions
# 479,251


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x).replace("0b", "") 
        y = bin(y).replace("0b", "") 
        
        leng = max(len(x),len(y))
        x = x.zfill(leng)
        y = y.zfill(leng)
        
        count = 0
        
        for i in range(leng):
            if (int(x[i]) ^ int(y[i])) != 0:
                count = count + 1
        
        return count
        
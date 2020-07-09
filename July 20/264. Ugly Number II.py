# 264. Ugly Number II
# Medium

# 1868

# 121

# Add to List

# Share
# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  

# 1 is typically treated as an ugly number.
# n does not exceed 1690.

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ht = {2:0,3:0,5:0}
        i2 = i3 = i5 = 0
        
        ugly = [0] * n
        ugly[0] = 1
        
        twox = 2
        threex = 3
        fivex = 5
        
        for i in range(1,n):
            
            ugly[i] = min(twox,threex,fivex)
            
            if ugly[i] == twox:
                ht[2] = ht[2]+1
                twox = ugly[ht[2]] * 2
            
            if ugly[i] == threex:
                ht[3] = ht[3]+1
                threex = ugly[ht[3]] * 3

            if ugly[i] == fivex:
                ht[5] = ht[5]+1
                fivex = ugly[ht[5]] * 5
                
        print(ugly)
        
        return ugly[-1]
                  
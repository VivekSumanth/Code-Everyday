# date:15/jun/20
# 204. Count Primes
# Easy

# 1898

# 591

# Add to List

# Share
# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Accepted
# 349,697
# Submissions
# 1,120,596

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        
        numbers = [True]*(n)
 
        p = 2
        while(p*p <= n):
            
            if numbers[p] == True:
                for i in range(p*p,n,p):
                    numbers[i] = False          
            p = p + 1
      
        j = numbers.count(True)

        return j-2
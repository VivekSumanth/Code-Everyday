# 905. Sort Array By Parity
# Easy

# 1168

# 76

# Add to List

# Share
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

 

# Example 1:

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

# Note:

# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        k = len(A)
        i = 0
        
        while(k):
            
            if A[i]%2 != 0:
                A.append(A[i])
                A.pop(i)
            else:
                i = i + 1
            k = k - 1
            
        return A


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = list()
        for each in A:
            if each % 2 == 0:
                result.insert(0,each)
            else:
                result.append(each)
                
        return result
                
# 46. Permutations
# Medium

# 4192

# 108

# Add to List

# Share
# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
# Accepted
# 638,167
# Submissions
# 1,001,273


class Solution(object):
    def recursion(self,lis,l,r,result):
        if l == r:
            result.append(lis[:])
        else:   
            for i in range(l,r+1):

                 lis[l],lis[i] = lis[i],lis[l]
                 self.recursion(lis,l+1,r,result)
                 lis[l],lis[i] = lis[i],lis[l]
                
        return result

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        l = 0 
        r = len(nums) - 1
        
        return self.recursion(nums,l,r,result)
#https://leetcode.com/problems/3sum/ 


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        for i in range(0,n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = n-1
            while(L<R):
                total = nums[i]+nums[L]+nums[R]
                if(total<0):
                    L = L+1
                elif total>0:
                    R = R-1
                else:
                    result.append([nums[i], nums[L],nums[R]])
                    while L<R and nums[L]==nums[L+1]:
                        L = L+1
                    while L<R and nums[R]==nums[R-1]:
                        R = R-1
                    L = L+1
                    R = R-1
        return result

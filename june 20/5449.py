# date: 27/jun/20
# 5449. Check If Array Pairs Are Divisible by k

# Difficulty:Medium

# Given an array of integers arr of even length n and an integer k.

# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

# Return True If you can find a way to do that or False otherwise.

 

# Example 1:

# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# Example 2:

# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
# Example 3:

# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
# Example 4:

# Input: arr = [-10,10], k = 2
# Output: true
# Example 5:

# Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
# Output: true
 

# Constraints:

# arr.length == n
# 1 <= n <= 10^5
# n is even.
# -10^9 <= arr[i] <= 10^9
# 1 <= k <= 10^5


def canArrange(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: bool
    """
    pairs = []
 
    for i in range(len(arr)):
        
        for j in range(len(arr)):
            
            if arr[i] != None and arr[j] != None and i != j and (arr[i] + arr[j]) % k == 0:
                print(arr[i],arr[j])
                pairs.append([arr[i],arr[j]])
                arr[i],arr[j] = None,None
                
    print(pairs)
    print(len(arr))
    print(len(pairs))
    if len(pairs) == len(arr)//2:
        return True
    else:
        return False

arr = [1,2,3,4,5,6,0,0,0,0]

k = 7
canArrange(arr, k)

# TLE
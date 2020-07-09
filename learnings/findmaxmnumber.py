
def findmaxm():
    maxm = 0
    i = 0
    nums = [11,22,13,34,15,6,17]
    
    def recursion(i,maxm):
        
        if i == len(nums):
            return maxm
        else:
            maxm = max(nums[:i+1])
            return recursion(i+1,maxm)

    return recursion(i,maxm)
    
print(findmaxm())
def maxnum(nums):
    
    hashtable = dict() 
    
    for i in range(len(nums)):
        
        if nums[i] in hashtable.keys():
            hashtable[nums[i]] = hashtable[nums[i]] + 1
        else:
            hashtable[nums[i]] = 1
    print(hashtable)
    


maxnum([1,3,2,1,4,1,1,2,2,5])

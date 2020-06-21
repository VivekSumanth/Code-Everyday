# use divide and conquer to divide 
# use sorting at end when individual elements are left 
# if left and right parts are sorted which means all same elements either occupy left half or right half.



def recursion(nums):
    if len(nums) > 1:
        mid     = len(nums)//2
        left    = nums[:mid:]
        right   = nums[mid::]
        
        left    = recursion(left)
        right   = recursion(right)
        
        print(left,right)
        nums = []
        
        while  len(left) and len(right):
            if left[0] < right[0]:
                nums.append(left[0])
                left.pop(0)
            else:
                nums.append(right[0])
                right.pop(0)
            
        for i in left:
            nums.append(i)
        
        for j in right:
            nums.append(j)
    
    return nums


value = (recursion([1,1,1,1,3,4]))
print(value[len(value)//2])
def majority(arr):
    
    if len(arr) > 1: 
        mid = (len(arr))//2
        print(arr[:mid],arr[mid::])
        left = majority(arr[:mid])
        right = majority(arr[mid::])
        print(left,right)
        
        if left == right:
            print(left)
            return left
        
        lcount = left.count(arr[:mid])
        rcount = right.count(arr[mid::])
        
        if lcount > mid + 1:
            return left
        elif rcount > mid + 1:
            return right
        else:
            return [0]
            
    return arr

arr = [1,2,1,3,1]
print(majority(arr))
# https://www.geeksforgeeks.org/find-whether-an-array-is-subset-of-another-array-set-1/

# Find whether an array is subset of another array | Added Method 3
# Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not. Both the arrays are not in sorted order. It may be assumed that elements in both array are distinct.
# Examples:

# Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
# Output: arr2[] is a subset of arr1[]

# Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4}
# Output: arr2[] is a subset of arr1[]



# Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3}
# Output: arr2[] is not a subset of arr1[]

def subset(arr1,arr2):
    
    hashtable = dict()
    
    for i in range(len(arr1)):
        
        if arr1[i] in hashtable.keys():
            hashtable[arr1[i]] = hashtable[arr1[i]] + 1
        else:
            hashtable[arr1[i]] = 1

    for k in arr2:
        
        if (k in hashtable and hashtable[k] <= 0) or k not in hashtable:

            return ('arr1 is not subset of arr2')
            break
        else:
            hashtable[k] = hashtable[k] - 1 
    
    return ('arr1 is subset or arr2')        

arr1 = [11,1,13,21,3,7]
arr2 = [11,3,7,1]
print(subset(arr1,arr2))

# timecomplexity : O(n) + O(n)
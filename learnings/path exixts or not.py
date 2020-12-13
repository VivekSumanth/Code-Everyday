#return if path exixts.
arr = [[0,1,1],[0,1,0],[0,1,0]]

def path(row,col,tar_row,tar_col):
    if row >= tar_row or col >= tar_col:
        return 
    if arr[row][col] == 1:
        return False
    if row == tar_row-1 and col == tar_col-1 and arr[row][col] == 0:
        return True
    
    move = path(row+1,col,len(arr),len(arr[0])) or path(row,col+1,len(arr),len(arr[0]))
    
    return move

path( 0,0,len(arr),len(arr[0]))


----------------------------------------------------------------------------------------------------------------------------------------------------------
# return path 
arr = [[0,1,1],[0,1,0],[0,0,0]]

def path(row,col,tar_row,tar_col,root):
    
    if row >= tar_row or col >= tar_col:
        return 
    
    if arr[row][col] == 1:
        return False
        
    if row == tar_row-1 and col == tar_col-1 and arr[row][col] == 0:
        root.append([row,col])
        return True
    root.append([row,col])
    move = path(row+1,col,len(arr),len(arr[0]),root) or path(row,col+1,len(arr),len(arr[0]),root)
    
    return root
    
print(path(0,0,len(arr),len(arr[0]),[]))
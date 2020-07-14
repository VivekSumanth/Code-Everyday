
#   left to right coloums
#   top to bottom rows


#   [   c1 c2 c3
#       [1,2,3]     r1
#       [4,5,6]     r2
#               ]

#    a12 - 1 is row 2 is coloums

#   [a00,a01,a02]
#   [a10,a11,a12]

#   a(row,coloums)


arr = [ [1,2,3],
        [4,5,6]
                ]
        
rows = len(arr)
coloums = len(arr[0])

arr[0][1] = 11

print(arr)

# declaring an empty matrix
mat = [[0 for i in range(coloums)] for j in range(rows)]
print(mat)


for i in range(rows):
    for j in range(coloums):
        print(arr[i][j])
        

# # A classroom has several students, half of whom are boys and half of whom are girls. You need to arrange all of them in a line for the morning assembly such that the following conditions are satisfied:

# # The students must be in order of non-decreasing height.
# # Two boys or two girls must not be adjacent to each other.
# # You have been given the heights of the boys in the array  and the heights of the girls in the array . Find out whether you can arrange them in an order which satisfies the given conditions. Print "YES" if it is possible, or "NO" if it is not.

# # For example, let's say there are  boys and  girls, where the boys' heights are  and the girls' heights are . These students can be arranged in the order , which is [2, 3, 4, 5, 6, 8]. Because this is in order of non-decreasing height, and no two boys or two girls are adjacent to each other, this satisfies the conditions. Therefore, the answer is "YES".

# # Input Format

# # The first line contains an integer, , denoting the number of test cases.

# # The first line of each test case contains an integer, , denoting the number of boys and girls in the classroom.

# # The second line of each test case contains  space separated integers, , denoting the heights of the boys.

# # The third line of each test case contains  space separated integers, , denoting the heights of the girls.

# # Constraints

# # Output Format

# # Print exactly  lines. In the  of them, print a single line containing "YES" if it is possible to arrange the students in the  test case, or "NO" if it is not.

# # Sample Input 0

# # 1
# # 2
# # 1 3
# # 2 4
# # Sample Output 0

# # YES
# # Explanation 0

# # The following arrangement would satisfy the given conditions: . This is because the boys and girls and separated, and the height is in non-decreasing order.

# # Sample Input 1

# # 2
# # 2
# # 1 2
# # 3 4
# # 3
# # 2 3 5
# # 1 3 4
# # Sample Output 1

# # NO
# # YES
# # Explanation 1

# # For the first test case, if we arrange them in non-decreasing order of heights, the arrangement would be . But this way, two boys (and two girls) are adjacent to each other. Therefore, the answer is "NO".

# # For the second test case, we can arrange them as . Therefore, the answer is "YES".





def arrangeStudents(a, b):
    # Write your code here
    # a = boys
    # b = girls 
    
    def sort(a):
        for i in range(1,len(a)):
            key = a[i]
            j = i-1
            while j>=0 and key < a[j]:
                a[j+1] = a[j]
                j = j-1
            a[j+1] = key 
        print(a)

    sort(a)
    sort(b)
    
    if(len(a)!=len(b)):
        print(False)

    lis = [0]
    if min(a)< min(b):
    #boys are small in height
        for i in range(len(a)):
            if a[i]<=b[i] and a[i] >= max(lis) and b[i] >= max(lis):
                
                lis.append(a[i])
                lis.append(b[i])
            else:
                lis.append('false')
        print(lis)
                 
    else:
        #girls are small in height
        for i in range(len(a)):
            if a[i] >= b[i] and a[i] >= max(lis) and b[i] >= max(lis):
                
                lis.append(a[i])
                lis.append(b[i])
            else:
                lis.append('false')
        print(lis)
    
    if 'false' in lis:
        print ('NO')
    else:
        print ('YES')
arrangeStudents([1,2,3,4,5],[1,2,3,4,5])





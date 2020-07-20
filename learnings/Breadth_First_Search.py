from collections import defaultdict 
  
def dictionary(lis,find):
    
    graph = defaultdict(list)
    
    for each in lis:
        graph[each[0]].append(each[1])
    
    print(graph)
    
    queue = [find]
    visited = [False]*len(graph)
    visited[find] = True
    
    while queue:
        s = queue.pop(0)
        print(s,end = " ")
        
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
        

dictionary([[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]],1)


# Output:

#     defaultdict(<class 'list'>, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})                                                                                                 
#     1 2 0 3    


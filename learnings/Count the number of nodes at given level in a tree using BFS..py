# Count the number of nodes at given level in a tree using BFS.
# Given a tree represented as undirected graph. Count the number of nodes at given level l. It may be assumed that vertex 0 is root of the tree.

# Examples:

# Input :   7
#           0 1
#           0 2
#           1 3
#           1 4 
#           1 5
#           2 6
#           2
# Output :  4

# Input : 6
#         0 1
#         0 2
#         1 3
#         2 4
#         2 5
#         2
# Output : 3

from collections import defaultdict 
  
def dictionary(lis,level):
    
    graph = defaultdict(list)
    
    for each in lis:
        graph[each[0]].append(each[1])
    
    print(graph)
    
    queue = [lis[0][0]]
    lev = -1
    
    while(queue):
        count = 0
        lev = lev + 1
        
        for i in range(len(queue)):
            s = queue.pop(0)
            count = count + 1
            for e in graph[s]:
                queue.append(e)
                
        if lev == level:
            print(count)
            break

dictionary([[0,1],[0,2],[1,3],[1,4],[1,5],[2,6]],2)
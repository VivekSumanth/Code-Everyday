from collections import defaultdict,Counter
class Graph:
    
    def setgraph(self,nodes):
        
        self.x = range(len(nodes))
        
        self.d = defaultdict(list)
        
        for i in range(len(nodes)):
            for j in (nodes[i]):
                self.d[self.x[i]].append(j)
        
        print(self.d)
        
    def checkcycle(self):
        visited = Counter(self.x)
        stack = list()
        check = []
        for start in self.d:
            visited[start] = 0
            stack.append(start)
            check.append(start)
            print('')
            print(check)
            
            while(stack):
                j = stack.pop()
                print(j, end = ' -> ')
                
                for i in self.d[j]:
                    if visited[i] == 1 :
                        stack.append(i)
                        visited[i] = 0
                    elif visited[i] == 0 and i in check:
                        print(i)
                        print('cycle')
                        break
                print('No cycle')
               
g = Graph()
g.setgraph([[1,2],[2],[0,3],[3]])
g.checkcycle()



#User function Template for python3
def isCyclic(g,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    # code here
    
    visited = [False]*(n+1)
    check = []
    print(g)
    for i in g.keys():
        lis = [i]
        visited[i] = True
        
        while(lis):
            temp = lis.pop()
            # print(temp)
            check.append(temp)
            for j in g[temp]:
                if visited[j] == False and j not in check:
                    lis.append(j)
                    visited[j] = True
                elif visited[j] == True and j not in check:
                    return 1
    return 0

print(isCyclic({0: [1], 1: [0], 2: [3, 4], 3: [2, 4], 4: [3, 2]},5))
print(isCyclic({0: [1], 1: [0, 2], 2: [1, 3], 3: [2]},4))
print(isCyclic({0: [1], 1: [0]},2))
print(isCyclic({0: [1], 1: [0]},1))
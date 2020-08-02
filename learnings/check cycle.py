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
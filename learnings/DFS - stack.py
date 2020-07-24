from collections import defaultdict,Counter

def dfs(nodes,start):
    
    x = list(map(chr,range(97,97+len(nodes))))
    
    d = defaultdict(list)
    
    for i in range(len(nodes)):
        for j in (nodes[i]):
            d[x[i]].append(j)
    
    visited = Counter(x)
    visited[start] = 0
    stack = list()
    stack.append(start)
    print(stack)
    
    while(stack):
        j = stack.pop()
        print(j)
        for i in d[j]:
            if visited[i] == 1:
                stack.append(i)
                visited[i] = 0
        

dfs([['b','c'],['a','d','e'],['e','a'],['b','e','f'],['d','f','c'],['d','e']],'a')


# more object oriented way of doing graph problems

from collections import defaultdict,Counter

class Graph:
    
    def setgraph(self,nodes):
        
        self.x = list(map(chr,range(97,97+len(nodes))))
        
        self.d = defaultdict(list)
        
        for i in range(len(nodes)):
            for j in (nodes[i]):
                self.d[self.x[i]].append(j)
    
    def dfs(self,start):
        
        visited = Counter(self.x)
        visited[start] = 0
        stack = list()
        stack.append(start)
        print(stack)
        
        while(stack):
            j = stack.pop()
            print(j)
            for i in self.d[j]:
                if visited[i] == 1:
                    stack.append(i)
                    visited[i] = 0
            
g = Graph()
g.setgraph([['b','c'],['a','d','e'],['e','a'],['b','e','f'],['d','f','c'],['d','e']])
g.dfs('b')

# Recusive Fashion

from collections import defaultdict,Counter

class Graph:
    
    def setgraph(self,nodes):
        
        self.x = list(map(chr,range(97,97+len(nodes))))
        
        self.d = defaultdict(list)
        
        for i in range(len(nodes)):
            for j in (nodes[i]):
                self.d[self.x[i]].append(j)
        
    
    def dfs(self,start):
        
        visited = Counter(self.x)

        def recursion(start):
            if visited[start] == 0:
                return start
                
            print(start)
            
            visited[start] = 0
            for each in self.d[start]:
                if visited[each] == 1:
                    return recursion(each)
        recursion(start)

            
g = Graph()
g.setgraph([['b','c'],['a','d','e'],['e','a'],['b','e','f'],['d','f','c'],['d','e']])
g.dfs('b')
# b e c f d a 
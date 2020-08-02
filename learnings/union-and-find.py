from collections import defaultdict,Counter

class Graph:
    
    def __init__(self,edges):
        self.vertices = range(len(edges))
        self.edges = edges
        self.graph = defaultdict(list)
        
        
    def makeGraph(self):
        for i in range(len(self.vertices)):
            self.graph[self.vertices[i]] = self.edges[i]
        print(self.graph)
        
    def makeedges(self):
        self.alledges = []
        for i in self.vertices:
            for j in self.graph[i]:
                k =[i,j]
                k.sort()
                if k not in self.alledges:
                   self.alledges.append(k) 
    
    def union_and_find(self,v,visited,parent):
        
        visited[v] = True
        
        for i in self.graph[v]: 
            # If the node is not visited then recurse on it 
            if  visited[i]==False :  
                if(self.isCyclicUtil(i,visited,v)): 
                    return True
            # If an adjacent vertex is visited and not parent of current vertex, 
            # then there is a cycle 
            elif  parent!=i: 
                return True
          
        return False
        
        
        


    def cyclic(self):
        visited =[False]*(len(self.alledges)) 
        for i in range(len(self.alledges)):
            if visited[i] == False:
                if (self.union_and_find(i,visited,-1) == True):
                    return True
        return False        
        
        

g = Graph([[],[2],[3],[1]])
g.makeGraph()
g.makeedges()
g.cyclic()
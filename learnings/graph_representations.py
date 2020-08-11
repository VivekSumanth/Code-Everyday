

# vertices are given

from collections import defaultdict
class Graph():
    
    def __init__(self,vertices):
        self.vertices = vertices
        
    
    def setgraph(self):
        grap = defaultdict(list)
        for i in range(len(self.vertices)):
            grap[i] = self.vertices[i]
        print(grap)
        
    

g = Graph([[1,2,3],[2,3,4]])
g.setgraph()

# edges are given

from collections import defaultdict
class Graph():
    
    def __init__(self,vertices):
        self.vertices = vertices
        
    
    def setgraph(self):
        self.graph = defaultdict(list)
        for i in self.vertices:
            self.graph[i[0]] = i[1]
        
        print(self.graph)

g = Graph([[1,0],[0,2],[2,0],[0,3],[3,4]])
g.setgraph()

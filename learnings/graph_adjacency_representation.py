from collections import defaultdict 
  
def dictionary(connections,vertices):
    
    if len(connections) != len(vertices):
        print('connections or vertices are wrong')
    
    graph = defaultdict(list)
    

    for each in range(len(vertices)):
        
        graph[vertices[each]] = (connections[each])
    
    print(graph)

dictionary([['b','c','d','e','f'],['c','e'],['d'],['e'],['f'],['c','g','h'],['f','h'],['f','g']],['a','b','c','d','e','f','g','h'])

# defaultdict(<class 'list'>, {'c': ['d'], 'f': ['c', 'g', 'h'], 'a': ['b', 'c', 'd', 'e', 'f'], 'd': ['e'], 'b': ['c', 'e'], 'e': ['f'],
#  'h': ['f', 'g'], 'g': ['f', 'h']})  


from collections import defaultdict 
  
def representations(lis):
    # Defining a dict 
    d = defaultdict(list)
    l = len(lis)
    r = list(map(chr,range(97,97+l)))
    
    for i in range(l):
        for k in lis[i]:
            d[r[i]].append(k)
        
    print(d)
      
    
    
representations([
    ['b', 'c', 'd', 'e', 'f'],
    ['c', 'e'],
    ['d'],
    ['e'],
    ['f'],
    ['c', 'g', 'h'],
    ['f', 'h'],
    ['f', 'g']
    ])

# defaultdict(<class 'list'>, {'f': ['c', 'g', 'h'], 'a': ['b', 'c', 'd', 'e', 'f'], 'b': ['c', 'e'], 'g': ['f', 'h'], 'c': ['d'], 'e': [
# 'f'], 'd': ['e'], 'h': ['f', 'g']})  

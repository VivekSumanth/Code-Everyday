
#   creation of a btree
#   adding nodes into btree
#   printing the nodes in DFS :
#            -> Preorder 
#            -> Inorder
#            -> Postorder 
#   printing the nodes in BFS:
#            -> Levelorder

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key
        
        
       
def preorder(root):
    
    if root != None:
        
        print(root.key, end = " ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root != None:
        
        inorder(root.left)
        print(root.key, end = " ")
        inorder(root.right)
        
def levelorder(root):
    print('\n')
    
    if root is None:
        return 0
        
    q = []
    q.append(root)
    while(len(q)):
        print(q[0].key, end = " " )
        temp = q.pop(0)
        
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)
            
    
def postorder(root):
    if root != None:
        
        postorder(root.left)
        postorder(root.right)  
        print(root.key, end = " ")

def insert(root,value):
    q = []
    q.append(root)
    
    while(len(q)):
        temp = q[0]
        q.pop(0)
        
        if temp.left is not None:
            q.append(temp.left)
        else:
            temp.left = Node(value)
            break
        if temp.right is not None:
            q.append(temp.right) 
        else:
            temp.right = Node(value)
            break

def height(root):
    
    if root is None:
        return 0
    
    ldepth = height(root.left)
    rdepth = height(root.right)
    
    if ldepth > rdepth:
        return ldepth+1
    else:
        return rdepth+1 
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

preorder(root)
print('preorder')
print('postorder\n')
postorder(root)
print('inorder\n')
inorder(root)
levelorder(root)

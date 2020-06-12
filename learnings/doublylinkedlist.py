class Node:
    def __init__(self, data):
        
        self.data = data
        self.next = None
        self.prev = None

class Ddl:
    
    def __init__(self):
        
        self.head = None
        
    def push(self,data):
        
        newnode = Node(data)
        newnode.next = self.head
        
        if self.head:
            self.head.prev = newnode
        
        self.head = newnode
        
    def print(self,node):
        
        while(node):
            print(node.data)
            last = node
            node = node.next
        
        while(last):
            print(last.data)
            last = last.prev

llist = Ddl()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.prev = llist.head

second.next = third
third.prev = second
llist.push(4)
llist.print(llist.head)
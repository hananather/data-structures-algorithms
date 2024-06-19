class Node: 
    def __init__(self, data):
        self.data  = data
        self.node = None

class Stacks:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top 
        self.top = new_node
        self.size += 1
    
            
        
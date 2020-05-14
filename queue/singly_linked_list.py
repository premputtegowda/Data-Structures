class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class SingleListLink:
    def __init__(self):
        self.head = None
        self.tail = None
        

    
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
           
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            self.tail = new_node 

    def pop(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            return value
            
    def size(self):

        current = self.head
        length = 0
        while current is not None:
            length +=1
            current = current.next
        return length
        

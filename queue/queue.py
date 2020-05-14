import sys
from singly_linked_list import Node
from singly_linked_list import SingleListLink

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = []
    
    def __len__(self):
        #pass
        self.size = len(self.storage)
        return self.size
        

    def enqueue(self, value):
        #pass
        return self.storage.append(value)
        

    def dequeue(self):
        #pass
        return self.storage.pop[0]



class Queue:
    def __init__(self):
        self.storage = SingleListLink()
        self.size = 0
        
    
    def __len__(self):
        self.size = self.storage.size()
        return self.size
        

    def enqueue(self, value):
        #pass
    
        return self.storage.append(value)
        

    def dequeue(self):
     
        return self.storage.pop()




class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
       



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            self.tail = new_node
            
    def remove_head(self):
        if self.head is None:
            return None
        else:
            current = self.head
            removed_head = self.head.value
            if current.next is not None:
                self.head = current.next
                if self.head.next is None:
                    self.tail = None
            else:
                
                self.head = None 
                self.tail = None

            return removed_head

    def get_max(self):
        if self.head is None:
            return None
        else:
            current = self.head
            max = self.head.value
            while current.next is not None:
                if current.next.value > max:
                    max = current.next.value
                current = current.next
        return max

    def remove_last_item(self):
        if self.head is None:
            return None
        else:
            current = self.head
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
    
    def contains(self, value):
        if self.head is None:
            return False
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    return True
                current = current.next
            return False

sl = LinkedList()
sl.add_to_tail(10)

print(sl.head.value)
print(sl.tail.value)
sl.remove_head()
print("head: ", sl.head)
print("max: ", sl.tail)
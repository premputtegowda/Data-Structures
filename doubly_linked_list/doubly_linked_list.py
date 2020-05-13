"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next #none
        #self.next = node(2,node(1),null)
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""



    def insert_before(self, value):
        current_prev = self.prev 

        self.prev = ListNode(value, current_prev, self) 
        
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    # None <-- Node 10--> 10 ---> 12 (tail)
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev 


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.head is not None:
            prev_head = self.head #2 none-10-none,
            #prev_head = node 10
            #curr_prev = none 
          
            prev_head.insert_before(value)
            self.head = prev_head.prev
            self.length += 1
            

    
        else:
            self.head = ListNode(value)
            self.tail = ListNode(value)
            self.length += 1
            

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        
        if self.head is None:
            return None
        
        elif self.head.next is not None:
            prev_head = self.head
            self.head = prev_head.next

            prev_head.delete()
            
            self.length -= 1
            return prev_head.value
        else:
            prev_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return prev_head.value

     ##old pro
        # value = self.head.value
        # print("next: ", self.head.next)
        # if self.head is None:
        #     return None
        
        # if self.head.next is None:    
        #     self.head = None
        #     self.tail = None
        #     self.length -= 1
            
        # else: # none - 10 - 11
        #     #none - 11-None
        #     prev_head = self.head
        #     self.head = prev_head.next
        #     prev_head.delete()
        #     print("headdd: ", self.head.value)
        #     self.length -= 1
        # return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # 10, 1, 2...
        new_node = ListNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
            self.length += 1
            
            

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is None:
            return None
        elif self.head.next is None:
            value=self.tail.value
            self.head = None
            self.tail = None
            self.length -=1
            return value
        elif self.tail is not None:
            value = self.tail.value
            previous = self.tail.prev
            self.tail = previous
            self.tail.next = None
            self.length -=1
            return value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        node.delete()
        self.add_to_head(node.value)
        self.length -= 1
        return self.head.value
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.head:
            self.remove_from_head()
        
            self.add_to_tail(node.value)
            return self.tail.value
        else:
        
            node.delete()
            self.add_to_tail(node.value)
            self.length -= 1
            return self.tail.value

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
           
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            print('do it')    
            node.delete()
       
        # if node is self.head:
        #     print("remove_from_head triggered")
        #     self.remove_from_head()
        # elif node is self.tail:
        #     self.remove_from_tail()
        # else:
        #     node.delete()
        #     self.length -= 1

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None:
            return None
        else:
            max = self.head.value
            current = self.head
            while current is not None:
                if current.value > max:
                    max = current.value
                current = current.next
            return max


dll = DoublyLinkedList() 
# print("head ", dll.head)
# print("tail ", dll.tail)
dll.add_to_tail(1)
dll.add_to_head(9)
print("before delete Head ssssss", dll.head.next.value)
dll.add_to_tail(6)

print("Before ", dll.head.next.next)
dll.delete(dll.head)


print("After Head ", dll.head.next)
print("After Tail ", dll.tail.value)
# dll.remove_from_head()
# print("After Head ", dll.head)
# print("After Tail ", dll.tail)
# print("head ",dll.head.value)
# print("tail ",dll.tail.value)

# dll.add_to_head(9)

# print("head next",dll.head.value)
# print("tail ", dll.tail.value)
# dll.add_to_tail(6)
# nextVal = dll.head.next
# print("head",dll.head.value)
# print("tail" , dll.tail.value)
# print("head next", dll.tail.value)
# print("head next next: ", dll.head.next.next)
# print("head next next: ", dll.tail.prev.next.value)



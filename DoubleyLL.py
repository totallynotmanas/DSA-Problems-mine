class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoubleyLinkedList:
    def __init__(self,head=None):
        self.head = head
        self.size = 0

    def add_first(self,data):
        
        #Adds a new node with the given data at the beginning of the linked list.
        
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def delete_first(self):
        
        #Deletes the first node from the linked list.
        
        if self.size == 0:
            print("Error: list is empty")
        else:
            removed_element = self.head 
            self.head = removed_element.next
            self.head.prev = None
            del removed_element
            self.size -= 1 
    
    def print_list(self):
        
        #Prints the elements of the linked list.
        
        if self.size == 0 :
            print("Error: List is empty")
        else:
            cur = self.head
            while cur:
                print(cur.data, end=" ")
                cur = cur.next
            print()
        
    def add_last(self,data):
        
        #Adds a new node with the given data at the end of the linked list.
        
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
        self.size += 1
    
    def delete_last(self):
        
        #Deletes the last node from the linked list.
        
        if self.size == 0:
            print("Error: list is empty")
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.prev.next = None
            del cur
            self.size -= 1
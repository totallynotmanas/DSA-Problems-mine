class Node:
    def __init__(self, data):
        self.data = data
        self.next: 'Node | None' = None

class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
      
    def delete_first(self):
        if self.size == 0: #gives an error message that the list is empty
            print("Error: list is empty")
        else:
            removed_element = self.head
            self.head = removed_element.next
            del removed_element
            self.size -= 1

    def print_list(self):
        if self.size == 0 : 
            print("Error: List is empty")
        else:
            for i in range(self.size):
                
                if i == 0:
                    print("[ head-->",str(self.head.data), end=",")
                    cur = self.head.next
                elif i == (self.size - 1):
                    print(str(cur.data),"]")
                else:
                    print(str(cur.data) , end=",")
                    cur=cur.next

    def add_last(self,data):
        new_node = Node(data)
        
        if self.size == 0:
            self.head = new_node
        else:                    
            cur = self.head
            for i in range(self.size):
                if i == (self.size - 1):
                    cur.next = new_node
                else:
                    cur = cur.next
        self.size += 1
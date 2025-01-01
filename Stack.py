#class that represents the node in a linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#class that represents the Stack using linked list
class Stack:
    def __init__(self):
        #head pointer of the stack
        self.head = None
        #size of the stack
        self.size = 0 
    
    #function that checks if the stack is in underflow conditions
    def is_empty(self):
        
        #if no head is found then the stack is in underflow condition thus empty
        return self.head is None
        
    #function that pushes a new element into the stack  
    def push(self,new_data):
        new_node = Node(new_data) #Node object that contains the data
        
        #checks if the memory allocation has failed for the new node
        if not new_node:
            print("\n stack overflow")
            return
        
        new_node.next = self.head #puts the value of the next link into the next attribute of the new_node object
        
        self.head = new_node #makes the new node as the head of the stack
        
        self.size += 1 #increases the size by one
    
    #removes and returns the top element of the stack
    def pop(self):
        
        #checking stack underflow condition
        if self.is_empty():
            print("\n stack underflow")
        else:
            temp = self.head #assinging the head of the stack to a temporary variable 
            
            self.head = self.head.next #makes the next element of the stack as the head
            
            temp_data = temp.data #gets the data to another variable so that it can be returned
            
            del temp #removes the previous top node
            
            self.size -= 1 #decreases the size by one
            
            return temp_data #returns the value of previous head
            
    
    #functions the display the top of the stack without the removing the element    
    def top(self):
        #check if the stack is in underflow condition
        if self.is_empty():
            print("\n stack underflow")
        else:
            return self.head.data #returns the top node of the stacks which is stored in the temp variable
        
    #function to display the whole stack
    def display(self):
        temp = Stack() #temporary stack to store the values only for the function
        
        #check if the stack is in underflow condition
        if self.is_empty():
            print("\n stack underflow")
        else:
            while not self.is_empty():
                temp_var = self.pop() #stores the top element
                print(temp_var,end="")
                temp.push(temp_var) #pushes the variables
            print("\n stack underflow")
            while not temp.is_empty():
                self.push(temp.pop())
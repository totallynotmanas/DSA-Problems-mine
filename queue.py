class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.first = None
        self.last = None
        
    def enqueue(self, data):
        new_node = node(data)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        if self.first == None:
            return None
        else:
            cur = self.first
            while cur.next != self.last:
                cur = cur.next
            cur.next = None
            self.last = cur

    
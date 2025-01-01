class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,data):
        new_node = node(data)
        if self.root is None:
            self.root = new_node
            self.size += 1
            return
        temp = self.root
        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    self.size += 1
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    self.size += 1
                    return
                temp = temp.right
        
    def search(self, data):
        temp = self.root
        while temp:
            if temp.data == data:
                return True 
            elif data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end = ' ')
            self.inorder(root.right)
            +3
        
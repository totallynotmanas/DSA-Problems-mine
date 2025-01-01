class node:
    def __init__(self,Emp_id, Name, Salary):
        self.Emp_id = Emp_id
        self.Name = Name
        self.Salary = Salary
        self.left = None
        self.right = None
    
    def isLeaf(self):
        return self.left == None and self.right == None
    
    def isInternal(self):
        return self.left != None or self.right != None
    
    def isRoot(self):
        return self.parent == None

class EMP_BST:
    def __init__(self):
        self.size = 0
        self.root = None
        self.ht = 0
    
    def insert(self,Emp_id, Name, Salary):
        new_node = node(Emp_id, Name, Salary)
        if self.size == 0:
            self.root = new_node
        else:
            cur = self.root
            while True:
                if new_node.Emp_id < cur.Emp_id:
                    if cur.left == None:
                        cur.left = new_node
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right == None:
                        cur.right = new_node
                        break
                    else:
                        cur = cur.right
        self.size += 1

    def search(self, Emp_id):
        cur = self.root
        while cur != None:
            if cur.Emp_id == Emp_id:
                return cur
            elif Emp_id < cur.Emp_id:
                cur = cur.left
            else:
                cur = cur.right
        print("Employee not found")
        return None
    
    def delete(self,Emp_id):
        cur = self.root
        parent = None
        while cur != None:
            if cur.Emp_id == Emp_id:
                break
            elif Emp_id < cur.Emp_id:
                parent = cur
                cur = cur.left
            else:
                parent = cur
                cur = cur.right
        if cur == None:
            print("Employee not found")
            return
        if cur.isLeaf():
            if cur.isRoot():
                self.root = None
            elif parent.left == cur:
                parent.left = None
            else:
                parent.right = None
            del cur
    
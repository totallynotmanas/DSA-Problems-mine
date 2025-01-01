class Node:
    def __init__(self,data,parent=None):
        self.data=data
        self.parent=parent
        self.left = None
        self.right = None

    def isInternal(self):
        return self.right==None or self.left==None
    

    def isExternal(self):
        return not self.isInternal()
    
class BinTree:
    def __init__(self):
        self.size = 0
        self.root = None
        self.ht = 0

    def getChildren(self,curnode):
        children = []
        if curnode.left != None:
            children.append(curnode.left)
        if curnode.right != None:
            children.append(curnode.right)
        return children
    
    def isRoot(self,curnode):
        return curnode == self.root


    def buildTree(self,eltlist):
        self.size = 0 
        nodelist= []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if (i != 0):
                if (eltlist[i] != -1):
                    tempnode = Node()
                    tempnode.data = eltlist[i]
                    if ((i%2) == 0):
                        nodelist[i // 2].left = tempnode
                    else:
                        nodelist[i // 2].right = tempnode
                    nodelist.append(tempnode)
                    self.size += 1
                else:
                    nodelist.append(None)
        
        self.root = nodelist[1]
        return nodelist
    
    def getSize(self):
        return self.size()
    
    def preorder(self,node):
        if node is None:
            return
        print(node.data,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
        
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data,end=" ")
    
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data,end=" ")
        self.inorder(node.right)

    def insert(self,data):
        new_node = Node(data)
        if self.size == 0:
            self.root = new_node
        else:
            

def main():
    BinTree1 = BinTree()
    f = open("input.txt","r")
    eltlist = f.readlines()




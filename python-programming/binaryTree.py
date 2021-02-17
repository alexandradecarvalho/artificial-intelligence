class Node:
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def getValue(self):
        return self.value

    def getParent(self):
        return self.parent

    def getChildren(self):
        return (self.left, self.right)
    def __str__(self):
        return ("Node=" + str(self.value) + "-> " + str(self.left) + ", " + str(self.right) + "\n")

class BinaryTree:
    def __init__(self,root_value):
        self.root = Node(root_value,None)

    def getRoot(self):
        return self.root
    
    def addNode(self,value,node = None):
        if not node:
            node = self.root
        if(value < node.value):
            if(node.left != None):
                self.addNode(value, node.left)
            else:
                node.left = Node(value,node)
        else:
            if(node.right != None):
                self.addNode(value, node.right)
            else:
                node.right = Node(value, node)

    def findNode(self,value, node = None):
        if not node:
            node = self.root
        if(value == node.value):
            return True
        elif(value < node.value and node.left != None):
            return self.findNode(value, node.left)
        elif(value > node.value and node.right != None):
            return self.findNode(value, node.right)
        else:
            return False

    def __str__(self):
        return ("Tree with root: " + str(self.root))

if __name__ == "__main__":
    btree = BinaryTree(5)
    btree.addNode(3)
    btree.addNode(4)
    btree.addNode(0)
    btree.addNode(8)
    btree.addNode(2)
    print(btree)

    print(btree.findNode(4))
    print(btree.findNode(6))
from _pytest.compat import getlocation

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        temp = self.root
        while temp:
            # print('k',temp.value)
            if new_val == temp.value:
                break
            if new_val < temp.value:
                if temp.left == None:
                    temp.left = Node(new_val)
                temp = temp.left
            elif new_val > temp.value:
                if temp.right == None:
                    temp.right = Node(new_val)
                temp = temp.right

    def printSelf(self):
        # Your code goes here
        temp = self.root
        self.getInorder(temp)
        
    def getInorder(self, node):
        if node:
            self.getInorder(node.left)
            print(node.value, end = ' ')
            self.getInorder(node.right)
        
    def search(self, find_val):
        # Your code goes here
        if find_val == None:
            return False
        temp = self.root
        while temp != None:
            if type(temp.value) == type(find_val) and  temp.value == find_val:
                return True
            if type(temp.value) == type(find_val) and find_val <= temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

tree = BST(4)
tree.insert(5)
tree.insert(1)
tree.insert(2)
tree.printSelf()
print(tree.search(5))
print(tree.search('f'))
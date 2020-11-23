class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if self.value:
            if d < self.value:
                if self.left is None:
                    self.left = Node(d)
                else:
                    self.left.insert(d)
            elif d > self.value:
                if self.right is None:
                    self.right = Node(d)
                else:
                    self.right.insert(d)
        else:
            self.value = d

    def find(self,d):
        if self.value < d:
            if self.right:
                return self.right.find(d)
            else:
                return False
        elif self.value > d:
            if self.left:
                return self.left.find(d)
            else:
                return False
        elif self.value == d:
            return True

    def preOrderPrint(self):
        print(self.value, end=" ")
        if self.left:
            self.left.preOrderPrint()
        elif self.right:
            self.right.preOrderPrint()

    def postOrderPrint(self):
        print(self.value, end=" ")
        if self.left:
            self.left.postOrderPrint()

        if self.right:
            self.right.postOrderPrint()
# :(
    def delete(self,key):
        pass


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,d):
        if self.root is None:
            self.root = Node(d)
        else:
            return self.root.insert(d)

    def find(self,d):
        if self.root.value is None:
            return False
        else:
            return self.root.find(d)

    def preOrderPrint(self):
        if self.root is None:
            print("Empty")
        else:
            self.root.preOrderPrint()
            print()

    def postOrderPrint(self):
        if self.root is None:
            print("Empty")
        else:
            self.root.postOrderPrint()
            print()

    def delete(self,d):
        if self.root is None:
            return False
        else:
            return self.root.delete(d)

t = Tree()
t.insert(20)
t.insert(10)
t.insert(5)
t.insert(15)
t.insert(17)
t.insert(30)
t.insert(25)
t.insert(35)
t.preOrderPrint()
print()
t.delete(20)
t.preOrderPrint()
print()
print(t.find(1))
print(t.find(35))

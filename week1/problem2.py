class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

    def get_val(self):
        return self.val

    def get_left(self):
        return self.left.get_val()
    def get_rigth(self):
        return self.right.get_val()

    def set_left(self, left):
        self.left = left
    def set_right(self, right):
        self.right = right

    def remove_left(self):
        self.left = None
    def remove_right(self):
        self.rigth = None

    def is_root(self):
        return self.parent == None


root = Node(0)
ch1 = Node(1, 0)
ch2 = Node(2, 0)
ch3 = Node(3, 1)
ch4 = Node(4, 1)

root.set_left(ch1)
ch1.set_left(ch3)
ch1.set_right(ch4)

print(root.get_left().get_left())

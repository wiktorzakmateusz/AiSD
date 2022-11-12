

class Node:
    def __init__(self, v, l = None , r = None):
        self.val = v
        self.left = l
        self.right = r


def printAll(root):
    if root is None:
        return

    print(root.val, end=" ")

    printAll(root.left)
    printAll(root.right)

class Stack:
    def __init__(self):
        self.lista = []

    def push(self, node):
        self.lista.append(node)

    def pop(self):
        elem = self.lista.pop()
        return elem

    def is_empty(self):
        if not self.lista:
            return True
        return False

def nrPrintAll(root):
    s = Stack()
    s.push(root)

    while not s.is_empty():
        p = s.pop()
        print(p.val, end = " ")
        if p.left is not None:
            s.push(p.left)
        if p.right is not None:
            s.push(p.right)



def main():
    root = Node(8)
    root.left = Node(7, Node(10), Node(3, None, Node(2)))
    root.right = Node(5, Node(1))

    #printAll(root)
    nrPrintAll(root)


if __name__ == '__main__':
    main()













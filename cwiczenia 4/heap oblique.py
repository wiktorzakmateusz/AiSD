


class Node:
    def __init__(self, v, l=None, r=None):
        self.left = l
        self.right = r
        self.val = v


def union(p1, p2):
    if p1.val < p2.val:
        p1, p2 = p2, p1

    if p1.right == None:
        p1.right = p2
    else:
        p1.right = union(p1.right, p2)

    p1.left, p1.right = p1.right, p1.left

    return p1

def insert(root, v):
    root = union(root, Node(v))
    return root
    
def del_max(root):
    root = union(root.left, root.right)
    return root







def main():
    pass



if __name__ == '__main__':
    main()



class Node:
    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

def Union(p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1

    if p1.val < p2.val:
        p1, p2 = p2, p1

    p = p1

    p.right = Union(p.right, p2)

    p.left, p.right = p.right, p.left

    return p

def DeleteMax(root):
    p = Union(root.left, root.right)
    return p

def Insert(root, v):
    return Union(root, Node(v))




def main():
    #p1
    p1 = Node(27,
                Node(20,
                    Node(9),
                    Node(16,
                        Node(7)
                    )
                ),
                Node(22,
                     Node(13,
                          Node(4)
                    )
                )
            )

    p2 = Node(24,
                Node(18,
                    Node(12),
                    Node(6,
                        Node(1)
                    )
                ),
                Node(23,
                     Node(2),
                     Node(12)
                )
            )

    p = Union(p1, p2)

    print(p.left.left.left.right.left.val)


if __name__ == '__main__':
    main()

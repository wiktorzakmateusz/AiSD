


class Node:
    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r
        if r:
            self.npl = r.npl + 1
        else:
            self.npl = 0

def Union(p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1

    if p1.val < p2.val:
        p1, p2 = p2, p1

    p = p1

    p.right = Union(p.right, p2)

    if p.left is None or p.left.npl < p.right.npl:
        p.left, p.right = p.right, p.left

    if p.right is None:
        p.npl = 0
    else:
        p.npl = p.right.npl + 1

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

    print(p.left.left.npl)


if __name__ == '__main__':
    main()


class Node:
    def __init__(self, k, h, prev, next, child):
        self.key = k
        self.h = h
        self.prev = prev
        self.next = next
        self.child = child

def merge_tree(p1, p2):
    if p1.key < p2.key:
        p1, p2 = p2, p1

    if p1.h == 0:
        p1.child = p2
    else:
        p1.child.prev.next = p2
        p2.prev = p1.child.prev
        p1.child.prev = p2

    p1.h += 1

    return p1


def extract_tree(head):
    p = head
    head = p.next
    head.prev = p.prev
    p.next = None
    p.prev = p
    return p

def union(p1,p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1

    if p1.h > p2.h:
        p1, p2 = p2, p1

    if p1.h < p2.h:
        t = extract_tree(p1)
        p = union(p1, p2)
        t.next = p
        t.prev = p.prev
        p.prev = t
        return t

    # if p1.h == p2.h

    t1 = extract_tree(p1)
    t2 = extract_tree(p2)
    t3 = merge_tree(t1,t2)
    p = union(p1,p2)
    return union(t3, p)

def insert(head, v):
    t = Node(v, 0, None, None, None)
    t.prev = t

    return union(head, t)

def max_elem(head):
    if head == None:
        return None
    p = head
    p_max = p
    while p:
        if p.key > p_max.key:
            p_max = p
        p = p.next
    return p_max.key

def del_max(head):
    if head == None:
        return None
    p = head
    p_max = p
    while p:
        if p.key > p_max.key:
            p_max = p
        p = p.next

    t = p_max.child
    if p_max.next:
        p_max.next.prev = p_max.prev
    else:
        head.prev = p_max.prev

    if p_max != head:
        p_max.prev.next = p_max.next
    else:
        head = head.next


    return union(head, t)











def main():
    pass




if __name__ == "__main__":
    main()
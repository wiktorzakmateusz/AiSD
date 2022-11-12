





class Node:

    Id = 0

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.id = Node.Id
        Node.Id = Node.Id + 1

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.sentinel = None

        if values is not None:
            self.add_multiple_nodes(values)

    def add_node(self, value):
        if self.head is None:
            self.head = Node(value, self.sentinel)
        else:
            self.head = Node(value, self.head)

    def add_multiple_nodes(self, values):
        for e in values:
            self.add_node(e)

    def __str__(self):
        if self.head == None:
            return None

        list = []
        p = self.head

        while p is not None:
            list.append(p.value)
            p = p.next

        return str(list)

    def search1(self, v):

        p = self.head

        while p is not None:
            if p.value == v:
                return p, p.id
            p = p.next

        return p

    def search2(self, v):
        if self.head is None:
            return None

        self.sentinel = Node(v)

        p = self.head

        while p.value != v:
           p = p.next

        if p == self.sentinel:
            return None

        return p.id




def main():
    list  = LinkedList([1,5,3,2])
    list.add_node(10)
    print(list)

    print(list.search2(7))


if __name__ == '__main__':
    main()











class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value

class LinkedList:
    def __init__(self, values=None):
        self.head = None

        if values is not None:
            self.add_multiple_nodes(values)

    def add_node(self, value):
        if self.head is None:
            self.head = Node(value)
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

    def sort(self):
        p = self.head
        if p == None:
            return

        list = []

        while p != None:
            list.append(p.value)
            p = p.next

        list.sort(reverse=True)

        big_list = LinkedList(list)

        self.head = big_list.head



    def insert(self, v):

        if self.head == None:
            self.head = Node(v)
            return

        if self.head.value > v:
            self.head = Node(v, self.head)
            return

        p = self.head

        while p.next != None and p.next.value < v:
            p = p.next

        p.next = Node(v, p.next)






def main():
    #tworzenie listy
    list  = LinkedList([1,5,3,2])
    list.add_node(10)
    print(list)

    #sortowanie listy
    list.sort()
    print(list)

    #insert
    list.insert(0)
    print(list)



if __name__ == '__main__':
    main()





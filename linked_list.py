class Node:
    def __inet__(self, data = None , next = None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self) -> None:
        self.head = None

    def insert_at_biginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("emtry linked list")
            return
        # create a iterable
        itr = self.head
        while itr:
            itr = itr.next
            print(self.head.data)














lil = Linked_list()
lil.insert_at_biginning(1)
lil.insert_at_biginning(2)
lil.insert_at_biginning(3)

lil.print()
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == "__main__":
    # assign the item values
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # connect the nodes
    linkedlist.head.next = second
    second.next = third

    while linkedlist.head != None:
        print(linkedlist.head.item, end="-")
        linkedlist.head = linkedlist.head.next

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self, data=None) -> None:
        self.head = Node(data) or None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, data):
        if self.head == None:
            raise("LinkedList is empty")
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        raise ValueError("Value not in Linked List")

    def size(self):
        index = 0
        current = self.head
        while current:
            index += 1
            current = current.next
        return index

    def remove(self, data):
        if self.head == None:
            raise ValueError("LinkedList is empty")
        current = self.head
        if current.data == data:
            self.head = current.next
            current = None
            return
        previous = None
        while current.next:
            previous = current
            current = current.next
            if current.data == data:
                previous.next = current.next
                

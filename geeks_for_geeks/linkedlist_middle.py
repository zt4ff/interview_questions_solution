"""
    Link: https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/
    Given a singly linked list, find the middle of the linked list. For example, if the given linked list is 1->2->3->4->5 then the output should be 3. 
    If there are even nodes, then there would be two middle nodes, we need to print the second middle element. For example, if given linked list is 1->2->3->4->5->6 then the output should be 4. 
"""

class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self, node=None) -> None:
        if node:
            self.head = Node(node)
        else:
            self.head = None
    
    def printList(self):
        current = self.head
        str = ""
        while current:
            str += f'{current.data} '
            current = current.next
        return str.rstrip()

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printMiddle(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data

from logging import setLoggerClass
import sys
sys.path.insert(0, '/home/kayode/Documents/Learning/interview_questions/data_structures')
import unittest
from linked_list import SinglyLinkedList

class LinkedListTestCases(unittest.TestCase):
    def setUp(self):
        self.linkedlist = SinglyLinkedList("first")
        self.linkedlist.add("second")

    def test_second_item_present(self):
        self.assertEqual(self.linkedlist.search("second").data, "second")

    def test_size_of_linkedlist(self):
        self.linkedlist.add("third")
        self.linkedlist.add("fourth")
        self.assertEqual(self.linkedlist.size(), 4)

    def test_remove_item(self):
        self.linkedlist.remove("third")
        self.assertEqual(self.linkedlist.size(), 3)


if __name__ == '__main__':    
    unittest.main()

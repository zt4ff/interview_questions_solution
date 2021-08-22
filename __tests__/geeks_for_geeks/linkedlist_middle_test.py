import unittest
import sys
sys.path.insert(0, "/home/kayode/Documents/Learning/interview_questions/geeks_for_geeks")
from linkedlist_middle import SinglyLinkedList
class TestMiddleLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.ll_one = SinglyLinkedList("1")
        self.ll_one.add("2")
        self.ll_one.add("3")
        self.ll_one.add("4")
        self.ll_one.add("5")
        self.ll_one.add("6")
        self.ll_one.add("7")
        self.ll_one.add("8")

    def test_print_function(self):
        self.assertEqual(self.ll_one.printList(), "8 7 6 5 4 3 2 1")

    def test_middle_node(self):
        self.assertEqual(self.ll_one.printMiddle(), "4")
        


if __name__ == "__main__":
    unittest.main()
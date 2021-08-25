import unittest
import sys
sys.path.insert(0,"/home/kayode/Documents/Learning/interview_questions/data_structures")
from queue_implementation import Queue 


class QueueImplementationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue(5)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)

    def test_queue_is_created(self):
        self.queue
        self.assertEqual(self.queue.total(), [1, 2, 3, 4, 5])

    def test_queue_rear(self):
        self.assertEqual(self.queue.que_rear(), 5)

    def test_dequeue(self):
        self.queue.dequeue()
        self.assertEqual(self.queue.que_front(), 2)

if __name__ == "__main__":
    unittest.main()
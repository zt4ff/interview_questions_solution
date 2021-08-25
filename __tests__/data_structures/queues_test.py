import unittest
import sys
sys.path.insert(0,"/home/kayode/Documents/Learning/interview_questions/data_structures")
import Queue from queue_implementation


class QueueImplementationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue(5)
        self.queue.enqueue(s1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)

    def test_queue_is_created(self):
        queue = self.queue
        self.assertEqual(queue(), [1, 2, 3, 4, 5])

    def test_dequeue(self):
        self.assertEqual(self.dequeue(), 1)

if __name__ == "__main__":
    unittest.main()
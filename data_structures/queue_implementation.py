"Implemetation using a fixed capacity Array"
class Queue(object):
    def __init__(self, capacity) -> None:
        self.Q = [None] * capacity
        self.rear = capacity - 1
        self.front = self.size = 0
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0
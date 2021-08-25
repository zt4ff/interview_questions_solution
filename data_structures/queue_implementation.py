"""
Implementation using static data structures of array
If we are actually remove the first item from memory, array would 
have to shift the whole items forwards which is a time complexity of
O(n), but can change the pointer to the next item while the dequeued 
item is nullified.
The con of this method is that if the array capacity is 30, you can only
make 30 insertions no matter the number of dequeues hence you get a 
constant time complexity of O(1) in all operations
"""
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

    def enqueue(self, item):
        if self.isFull():
            print("queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size += 1

    def que_rear(self):
        if self.isEmpty():
            print("queue is empty")
            return
        return self.Q[self.rear]

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    def que_front(self):
        if self.isEmpty():
            print("queue is empty")
            return
        return self.Q[self.front]

    def total(self):
        return self.Q

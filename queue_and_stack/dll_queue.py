import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# Should have the methods: enqueue, dequeue, and len.
# enqueue should add an item to the back of the queue.
# dequeue should remove and return an item from the front of the queue.
# len returns the number of items in the queue.


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def len(self):
        pass

import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# Should have the methods: enqueue, dequeue, and len.
# enqueue should add an item to the back of the queue.
# dequeue should remove and return an item from the front of the queue.
# len returns the number of items in the queue.


# # Simple example from g4g
# # Function to initialise the node object
# class Node:
#     def __init__(self, data):
#         self.data = data    # Assign data
#         self.next = None    # Initialize next as null
# # Linked List class contains a Node object
# class LinkedList:
#     # Function to initialize head
#     def __init__(self):
#         self.head = None


class Queue:
    def __init__(self):
        # Start size at 0
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Import linked list
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add to head, increase size, return size
        self.storage.add_to_head(value)
        self.size += 1
        return self.size

    def dequeue(self):
        # Check to see if the list length is less than or 0
        # If zero, can't allow dequeue
        if self.size <= 0:
            return None
        # Decrease size by 1
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size


# Store the class in a variable
# All the cool kids are doing it
q = Queue()
###################################
# # 10
# # head
# # 10 <-> 11
# # tail   head
# # 10 <-> 11 <-> 12
# # tail          head
# # 10 <-> 11 <-> 12 <-> 13
# # tail                 head
# # 11 <-> 12 <-> 13
# # tail          head
# # 12 <-> 13
# # tail   head
###################################
print(q.enqueue(10), q.enqueue(11), q.enqueue(12), q.enqueue(13))
print(q.dequeue())  # Results in 10, the tail removed
print(q.dequeue())  # Results in 10, the tail removed
print(q.len())  # 2

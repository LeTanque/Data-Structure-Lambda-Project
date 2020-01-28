import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)
        return self.size

    def pop(self):
        if self.size <= 0:
            return None
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size


stk = Stack()
print(stk.push(11), stk.push(12))
print(stk.pop())
print(stk.pop())
print(stk.push(13), stk.push(14), stk.push(15))
print(stk.len())

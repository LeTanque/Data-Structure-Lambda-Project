import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:

    # Our LRUCache class keeps track of the max number of nodes it
    # can hold, the current number of nodes it is holding, a doubly-
    # linked list that holds the key-value entries in the correct
    # order, as well as a storage dict that provides fast access
    # to every node stored in the cache.
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dll = DoublyLinkedList()
        self.storage = dict()   # Empty dict
        # self.storage = {}   # same

    # Retrieves the value associated with the given key. Also
    # needs to move the key-value pair to the end of the order
    # such that the pair is considered most-recently used.
    # Returns the value associated with the key or None if the
    # key-value pair doesn't exist in the cache.
    def get(self, key):
        # if key not in self.storage:
        #     return None
        # recent_value = self.storage[key]
        # del self.storage[key]
        # self.storage[key] = recent_value
        # return self.storage[key].value
        #
        # # Alternatively
        # # Check to see if key is in storage
        if key in self.storage:
            # Set the storage at index to node
            node = self.storage[key]
            # move node to end of linked list
            self.dll.move_to_end(node)
            # Return the value of node
            return node.value[1]
        else:
            return None

    # Adds the given key-value pair to the cache. The newly-
    # added pair should be considered the most-recently used
    # entry in the cache. If the cache is already at max capacity
    # before this entry is added, then the oldest entry in the
    # cache needs to be removed to make room. Additionally, in the
    # case that the key already exists in the cache, we simply
    # want to overwrite the old value associated with the key with
    # the newly-specified value.
    def set(self, key, value):
        # node = self.dll.add_to_head(value)
        # if key not in self.storage:
        #     self.storage[key] = node
        # elif len(self.storage) >= self.limit:
        #     for key in self.storage:
        #         del self.storage[key]
        #         break
        #     self.storage[key] = node
        # else:
        #     self.storage[key] = node

        # # Alternately
        # # if the key is already in linked list,
        # # move the key to the end (newest)
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.dll.move_to_end(node)
            return

        # # If by adding an item we are at the limit,
        # # remove the head (oldest)
        # # then make the size smaller
        if self.size == self.limit:
            del self.storage[self.dll.head.value[0]]
            self.dll.remove_from_head()
            self.size -= 1

        # # Add to tail the key val pair
        # # add to storage
        # # then increase the size by one
        self.dll.add_to_tail((key, value))
        self.storage[key] = self.dll.tail
        # self.storage[key] = value
        self.size += 1


lru = LRUCache(3)
lru.set("item1", "a")
lru.set("item2", "b")
lru.set("item3", "c")
lru.set("item2", "z")
lru.get("item1")
lru.get("item2")

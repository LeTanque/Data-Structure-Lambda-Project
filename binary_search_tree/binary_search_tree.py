import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


# Binary Search Tree is a node-based binary tree:
# The left subtree of a node contains only nodes
# with keys lesser than the node’s key.
# The right subtree of a node contains only nodes
# with keys greater than the node’s key.
# The left and right subtree each must also be a
# binary search tree.

# # WIKIPEDIA
# binary search, also known as half-interval search,
# [1] logarithmic search,[2] or binary chop,[3] is a
# search algorithm that finds the position of a target
# value within a sorted array.

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Each node needs to become itself a BST
    # Insert the given value into the tree
    def insert(self, value):
        # Compare root now
        if value < self.value:
            # if lesser go left child
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:   # Value is >= Node
            # if greater go right child
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                # If something is already there, recurse
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # JUst go right ->
        # BST most right is biggest
        # If there is nothing more right
        # You are at the largest node.
        if not self.right:
            return self.value
        else:
            return self.right.get_max()
        # ############ ALTERNATE
        # # Create a ref to the current node and update
        # # it as we traverse the tree
        # max_value = self.value
        # current = self  # < --- This is a cursor!
        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        # return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # The purpose of this method is to call the
        # same function on each node in the tree
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# # QUESTIONS
# Are hash tables more space performant, time performant
# or both?
#
# In my limited exp, they appear to be improve space
# complexity, but only nominal improvements to time
# complexity. Are my results atypical?
#
# If hash maps do indeed improve space performance more so
# than time, why?
# Is it because by having lower space requirements,
# hash tables decrease the time all subsequent operations
# take? So the processor can focus on other tasks and more
# data can be placed in RAM than without?
#
# Are we basically optimizing the processor with RAM
# when using a hash map?
#
# In what situations is the binary search tree pattern
# something we will use professionally, other than
# whiteboard challenges, in your opinion?
#
# Do we learn BST because it's a precursor to graphs?
# Is BST related to graphs?
#

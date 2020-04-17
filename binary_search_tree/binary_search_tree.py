import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if not self.value:
            self.value = value
            return

        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
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
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)                          # recurse down left branch
            print(node.value)                                       # current value        
            self.in_order_print(node.right)                         # recurse down right branch
        else:
            return

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()                                             # initialize a queue
        queue.enqueue(node)                                         # push root to queue
        while queue.len() > 0:                                      # while queue is not empty
            popped = queue.dequeue()                                # pop top item out of queue into temp variable
            print(popped.value)                                     # do the thing
            if popped.left:                                         # if temp has left put into queue
                queue.enqueue(popped.left)
            if popped.right:                                        # if temp has right put into queue
                queue.enqueue(popped.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()                                             # initialize a stack
        stack.push(node)                                            # push root to stack
        while stack.len() > 0:                                      # while stack is not empty
            popped = stack.pop()                                    # pop top item out of stack into temp
            print(popped.value)                                     # do the thing
            if popped.left:                                         # if temp has left put into stack
                stack.push(popped.left)
            if popped.right:                                        # if temp has right put into stack
                stack.push(popped.right)










    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

                                                            # Hint: Since our cache is going to be storing key-value pairs, we might want to use a structure that is adept at handling those.
                                                            # Tuples?

    def __init__(self, limit=10):
        self.limit = limit                                  # setting limit equal to input or default
        self.size = 0                                       # starting size
        self.entries = DoublyLinkedList()                   # init DLL class called 'entries' to contain LRU-MRU entries
        self.storage = {}                                   # empty storage dictionary to store all DLL values for quick access

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:                             # if the storage dict contains the provided key
            entry = self.storage[key]                       # declare an new node 'entry' equal to that value
            self.entries.move_to_end(entry)                 # and then move that node 'entry' to the end of DLL entries as it is now the MOST recently used (MRU)
            return entry.value[1]                           # return the value associated with 'entry' var.   (key, value) => value at 1 index!!!! (NOTE NOTE NOTE)
        else:
            return None                                     # if the key is not within self.storage, return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:                             # if the provided key already exists in the dict (check FIRST bc limit might be reached but we can still overwrite!)
            entry = self.storage[key]                       # grabbing the existing node with provided key and setting it equal to var 'entry'
            entry.value = (key, value)                      # resetting the value of 'entry' to the provided key value pair tuple from params
            self.entries.move_to_end(entry)                 # moving 'entry' to the end of DLL 'entries' as it is now most recently used
            return                                          # nothing else needs to be done! return here
        
        if self.size is self.limit:                         # if the limit is already maxed out
            del self.storage[self.entries.head.value[0]]    # remove LRU from 'storage' by grabbing key of value at head of 'entries' DLL.    (key, value) => key at 0 index!!!! (NOTE NOTE NOTE)
            self.entries.remove_from_head()                 # remove LRU from 'entries' by just removing the head
            self.size -= 1                                  # decrement size
                                                            # once that is done, we can proceed as usual to line 56

        self.entries.add_to_tail((key, value))              # add the new key value pair tuple to end of DLL 'entries' as the MRU node
        self.storage[key] = self.entries.tail               # add that node to the dict by the provided key
        self.size += 1                                      # increment size
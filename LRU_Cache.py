# Meta Question
# Solved using Doubly Linked List
# Neetcode: https://www.youtube.com/watch?v=7ABFKPK2hD4&ab_channel=NeetCode
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Map key to Node
        # Initialize dummy head and tail nodes to simplify operations
        self.head = Node(0, 0)  # points to least recently used
        self.tail = Node(0, 0)  # points to most recently used
        # Initially connect head and tail dummy nodes as it is a doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Removes node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node) -> None:
        """Adds node right before the tail (most recently used)."""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move accessed node to the tail to mark it as recently used
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the old node if key exists
            self._remove(self.cache[key])
        # Create and add the new node
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node

        # If the cache exceeds capacity, remove the least recently used node
        if len(self.cache) > self.capacity:
            lru = self.head.next  # Node after dummy head is least recently used
            self._remove(lru)
            del self.cache[lru.key]


####################################################

from collections import OrderedDict


# Using collections.OrderedDict()
class LRUCache1:
    def __init__(self, capacity: int):
        # Initialize an OrderedDict to maintain the order of access
        self.lru = OrderedDict()
        # Set the maximum capacity of the cache
        self.capacity = capacity

    # Time: O(1)
    def get(self, key: int) -> int:
        # If the key is not present in the cache, return -1
        if key not in self.lru:
            return -1

        # Move the accessed key to the end to mark it as recently used
        self.lru.move_to_end(key, last=True)
        # Return the value associated with the key
        return self.lru[key]

    # Time: O(1)
    def put(self, key: int, value: int) -> None:
        # If the key is already present, move it to the end to mark it as recently used
        if key in self.lru:
            self.lru.move_to_end(key)

        # Insert or update the key-value pair
        self.lru[key] = value

        # If the cache exceeds its capacity, remove the least recently used (LRU) item
        if len(self.lru) > self.capacity:
            self.lru.popitem(last=False)  # Removes the first (LRU) item

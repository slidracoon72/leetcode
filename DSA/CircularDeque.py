# LC-641 Design Circular Deque
class MyCircularDeque:

    def __init__(self, k: int):
        # Initialize the deque with a fixed size k
        self.deque = [0] * k  # Use a list to represent the deque
        self.max_size = k  # Maximum size of the deque
        self.front = 0  # Points to the front element
        self.rear = -1  # Points to the rear element
        self.size = 0  # Keeps track of the current size of the deque

    def insertFront(self, value: int) -> bool:
        # Add an item at the front
        if self.isFull():
            return False  # Can't insert if the deque is full
        self.front = (self.front - 1) % self.max_size  # Move front pointer backward
        self.deque[self.front] = value  # Insert the value at the new front
        self.size += 1  # Increment the size
        return True

    def insertLast(self, value: int) -> bool:
        # Add an item at the rear
        if self.isFull():
            return False  # Can't insert if the deque is full
        self.rear = (self.rear + 1) % self.max_size  # Move rear pointer forward
        self.deque[self.rear] = value  # Insert the value at the new rear
        self.size += 1  # Increment the size
        return True

    def deleteFront(self) -> bool:
        # Remove an item from the front
        if self.isEmpty():
            return False  # Can't delete if the deque is empty
        self.front = (self.front + 1) % self.max_size  # Move front pointer forward
        self.size -= 1  # Decrement the size
        return True

    def deleteLast(self) -> bool:
        # Remove an item from the rear
        if self.isEmpty():
            return False  # Can't delete if the deque is empty
        self.rear = (self.rear - 1) % self.max_size  # Move rear pointer backward
        self.size -= 1  # Decrement the size
        return True

    def getFront(self) -> int:
        # Get the front item
        if self.isEmpty():
            return -1  # Return -1 if deque is empty
        return self.deque[self.front]  # Return the front element

    def getRear(self) -> int:
        # Get the rear item
        if self.isEmpty():
            return -1  # Return -1 if deque is empty
        return self.deque[self.rear]  # Return the rear element

    def isEmpty(self) -> bool:
        # Check if the deque is empty
        return self.size == 0  # If size is 0, deque is empty

    def isFull(self) -> bool:
        # Check if the deque is full
        return self.size == self.max_size  # If size equals max_size, deque is full

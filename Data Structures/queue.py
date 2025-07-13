"""
Enhanced Queue Implementation
============================

A comprehensive queue data structure implementation with additional features:
- Basic queue operations (enqueue, dequeue, peek)
- Size and empty checks
- Priority queue functionality
- Circular queue implementation
- Thread-safe operations
- Error handling
- Practical examples and applications

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)
- Search: O(n)
- Size: O(1)
- Empty: O(1)

Space Complexity: O(n) where n is the number of elements
"""

from collections import deque
from typing import Any, Optional, List, Tuple
import threading
import time
import heapq


class Queue:
    """
    A queue implementation using deque for efficient operations.
    
    Attributes:
        buffer: Internal deque container for storing elements
        max_size: Maximum size limit (None for unlimited)
        lock: Thread lock for thread-safe operations
    """
    
    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize an empty queue.
        
        Args:
            max_size: Maximum number of elements allowed (None for unlimited)
        """
        self.buffer = deque()
        self.max_size = max_size
        self.lock = threading.Lock()
    
    def enqueue(self, item: Any) -> bool:
        """
        Add an item to the end of the queue.
        
        Args:
            item: The item to add to the queue
            
        Returns:
            True if successful, False if queue is full
            
        Raises:
            OverflowError: If queue is full and max_size is set
        """
        with self.lock:
            if self.max_size is not None and len(self.buffer) >= self.max_size:
                raise OverflowError("Queue is full")
            
            self.buffer.append(item)
            return True
    
    def dequeue(self) -> Any:
        """
        Remove and return the first item from the queue.
        
        Returns:
            The first item from the queue
            
        Raises:
            IndexError: If queue is empty
        """
        with self.lock:
            if self.is_empty():
                raise IndexError("Queue is empty")
            
            return self.buffer.popleft()
    
    def peek(self) -> Any:
        """
        Return the first item without removing it.
        
        Returns:
            The first item from the queue
            
        Raises:
            IndexError: If queue is empty
        """
        with self.lock:
            if self.is_empty():
                raise IndexError("Queue is empty")
            
            return self.buffer[0]
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.buffer) == 0
    
    def is_full(self) -> bool:
        """Check if the queue is full (only if max_size is set)."""
        if self.max_size is None:
            return False
        return len(self.buffer) >= self.max_size
    
    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self.buffer)
    
    def clear(self) -> None:
        """Remove all items from the queue."""
        with self.lock:
            self.buffer.clear()
    
    def contains(self, item: Any) -> bool:
        """Check if an item exists in the queue."""
        return item in self.buffer
    
    def to_list(self) -> List[Any]:
        """Convert queue to a list (front to back)."""
        return list(self.buffer)
    
    def __len__(self) -> int:
        """Return the number of items in the queue."""
        return len(self.buffer)
    
    def __str__(self) -> str:
        """String representation of the queue."""
        if self.is_empty():
            return "Queue([])"
        
        items = list(self.buffer)
        return f"Queue({items})"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return self.__str__()
    
    def __bool__(self) -> bool:
        """Return True if queue is not empty."""
        return not self.is_empty()


class PriorityQueue:
    """
    A priority queue implementation using heapq.
    
    Attributes:
        heap: Internal heap for storing (priority, item) pairs
        max_size: Maximum size limit (None for unlimited)
        lock: Thread lock for thread-safe operations
    """
    
    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize an empty priority queue.
        
        Args:
            max_size: Maximum number of elements allowed (None for unlimited)
        """
        self.heap = []
        self.max_size = max_size
        self.lock = threading.Lock()
    
    def enqueue(self, item: Any, priority: int = 0) -> bool:
        """
        Add an item with priority to the queue.
        
        Args:
            item: The item to add
            priority: Priority of the item (lower = higher priority)
            
        Returns:
            True if successful, False if queue is full
        """
        with self.lock:
            if self.max_size is not None and len(self.heap) >= self.max_size:
                return False
            
            heapq.heappush(self.heap, (priority, item))
            return True
    
    def dequeue(self) -> Any:
        """
        Remove and return the highest priority item.
        
        Returns:
            The highest priority item
            
        Raises:
            IndexError: If queue is empty
        """
        with self.lock:
            if self.is_empty():
                raise IndexError("Priority queue is empty")
            
            return heapq.heappop(self.heap)[1]
    
    def peek(self) -> Any:
        """
        Return the highest priority item without removing it.
        
        Returns:
            The highest priority item
            
        Raises:
            IndexError: If queue is empty
        """
        with self.lock:
            if self.is_empty():
                raise IndexError("Priority queue is empty")
            
            return self.heap[0][1]
    
    def is_empty(self) -> bool:
        """Check if the priority queue is empty."""
        return len(self.heap) == 0
    
    def size(self) -> int:
        """Return the number of items in the priority queue."""
        return len(self.heap)
    
    def clear(self) -> None:
        """Remove all items from the priority queue."""
        with self.lock:
            self.heap.clear()
    
    def __str__(self) -> str:
        """String representation of the priority queue."""
        if self.is_empty():
            return "PriorityQueue([])"
        
        items = [item for _, item in sorted(self.heap)]
        return f"PriorityQueue({items})"


class CircularQueue:
    """
    A circular queue implementation with fixed size.
    
    Attributes:
        capacity: Maximum capacity of the queue
        buffer: Internal list for storing elements
        front: Index of the front element
        rear: Index of the rear element
        size: Current number of elements
    """
    
    def __init__(self, capacity: int):
        """
        Initialize a circular queue with given capacity.
        
        Args:
            capacity: Maximum capacity of the queue
        """
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, item: Any) -> bool:
        """
        Add an item to the circular queue.
        
        Args:
            item: The item to add
            
        Returns:
            True if successful, False if queue is full
        """
        if self.is_full():
            return False
        
        self.rear = (self.rear + 1) % self.capacity
        self.buffer[self.rear] = item
        self.size += 1
        return True
    
    def dequeue(self) -> Any:
        """
        Remove and return the first item from the circular queue.
        
        Returns:
            The first item from the queue
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Circular queue is empty")
        
        item = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def peek(self) -> Any:
        """
        Return the first item without removing it.
        
        Returns:
            The first item from the queue
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Circular queue is empty")
        
        return self.buffer[self.front]
    
    def is_empty(self) -> bool:
        """Check if the circular queue is empty."""
        return self.size == 0
    
    def is_full(self) -> bool:
        """Check if the circular queue is full."""
        return self.size == self.capacity
    
    def get_size(self) -> int:
        """Return the number of items in the circular queue."""
        return self.size
    
    def clear(self) -> None:
        """Remove all items from the circular queue."""
        self.buffer = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def __str__(self) -> str:
        """String representation of the circular queue."""
        if self.is_empty():
            return f"CircularQueue({self.capacity}, [])"
        
        items = []
        for i in range(self.size):
            idx = (self.front + i) % self.capacity
            items.append(self.buffer[idx])
        
        return f"CircularQueue({self.capacity}, {items})"


class QueueApplications:
    """Collection of common queue applications and algorithms."""
    
    @staticmethod
    def breadth_first_search(graph: dict, start: Any) -> List[Any]:
        """
        Breadth-first search using queue.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        queue = Queue()
        visited = set()
        result = []
        
        queue.enqueue(start)
        visited.add(start)
        
        while not queue.is_empty():
            vertex = queue.dequeue()
            result.append(vertex)
            
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
        
        return result
    
    @staticmethod
    def level_order_traversal(root) -> List[List[Any]]:
        """
        Level order traversal of binary tree using queue.
        
        Time Complexity: O(n)
        Space Complexity: O(w) where w is max width
        """
        if not root:
            return []
        
        queue = Queue()
        queue.enqueue(root)
        result = []
        
        while not queue.is_empty():
            level_size = queue.size()
            level = []
            
            for _ in range(level_size):
                node = queue.dequeue()
                level.append(node.val)
                
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            
            result.append(level)
        
        return result
    
    @staticmethod
    def sliding_window_max(arr: List[int], k: int) -> List[int]:
        """
        Find maximum element in each sliding window using deque.
        
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        if not arr or k <= 0:
            return []
        
        result = []
        dq = deque()
        
        for i in range(len(arr)):
            # Remove elements outside the window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove smaller elements from the back
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            
            dq.append(i)
            
            # Add maximum to result
            if i >= k - 1:
                result.append(arr[dq[0]])
        
        return result
    
    @staticmethod
    def task_scheduler(tasks: List[str], n: int) -> int:
        """
        Task scheduler with cooldown period using priority queue.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # Count frequency of each task
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        # Create priority queue with negative frequencies
        pq = PriorityQueue()
        for task, count in freq.items():
            pq.enqueue((task, count), -count)
        
        time = 0
        while not pq.is_empty():
            temp = []
            
            for _ in range(n + 1):
                if not pq.is_empty():
                    task, count = pq.dequeue()
                    if count > 1:
                        temp.append((task, count - 1))
                    time += 1
                else:
                    if temp:  # If there are remaining tasks
                        time += 1
                    break
            
            # Re-add remaining tasks
            for task, count in temp:
                pq.enqueue((task, count), -count)
        
        return time


def demonstrate_queue_operations():
    """Demonstrate various queue operations."""
    print("=== Queue Operations Demo ===")
    
    # Create a queue
    queue = Queue(max_size=5)
    print(f"Created queue: {queue}")
    print(f"Is empty: {queue.is_empty()}")
    print(f"Size: {queue.size()}")
    
    # Enqueue elements
    elements = [1, 2, 3, 4, 5]
    for elem in elements:
        queue.enqueue(elem)
        print(f"Enqueued {elem}, Queue: {queue}")
    
    # Try to enqueue more (should raise error)
    try:
        queue.enqueue(6)
    except OverflowError as e:
        print(f"Error: {e}")
    
    # Peek and dequeue
    print(f"Peek: {queue.peek()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"After dequeue: {queue}")
    
    # Contains
    print(f"Contains 2: {queue.contains(2)}")
    print(f"Contains 10: {queue.contains(10)}")
    
    # Clear
    queue.clear()
    print(f"After clear: {queue}")


def demonstrate_priority_queue():
    """Demonstrate priority queue operations."""
    print("\n=== Priority Queue Demo ===")
    
    pq = PriorityQueue()
    
    # Add items with priorities
    items = [("Task A", 3), ("Task B", 1), ("Task C", 2), ("Task D", 1)]
    for item, priority in items:
        pq.enqueue(item, priority)
        print(f"Added {item} with priority {priority}")
    
    print(f"Priority Queue: {pq}")
    
    # Dequeue items (should come out in priority order)
    while not pq.is_empty():
        item = pq.dequeue()
        print(f"Dequeued: {item}")


def demonstrate_circular_queue():
    """Demonstrate circular queue operations."""
    print("\n=== Circular Queue Demo ===")
    
    cq = CircularQueue(3)
    print(f"Created circular queue: {cq}")
    
    # Enqueue elements
    for i in range(4):
        success = cq.enqueue(i)
        print(f"Enqueue {i}: {success}, Queue: {cq}")
    
    # Dequeue elements
    for _ in range(2):
        item = cq.dequeue()
        print(f"Dequeued: {item}, Queue: {cq}")
    
    # Enqueue more
    cq.enqueue(10)
    print(f"After enqueue 10: {cq}")


def demonstrate_queue_applications():
    """Demonstrate queue applications."""
    print("\n=== Queue Applications Demo ===")
    
    # BFS
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    bfs_result = QueueApplications.breadth_first_search(graph, 'A')
    print(f"BFS starting from A: {bfs_result}")
    
    # Sliding window max
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    window_max = QueueApplications.sliding_window_max(arr, k)
    print(f"Sliding window max for {arr} with k={k}: {window_max}")
    
    # Task scheduler
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    time_needed = QueueApplications.task_scheduler(tasks, n)
    print(f"Time needed for tasks {tasks} with cooldown {n}: {time_needed}")


def demonstrate_thread_safe_operations():
    """Demonstrate thread-safe queue operations."""
    print("\n=== Thread-Safe Queue Demo ===")
    
    queue = Queue(max_size=10)
    
    def producer():
        for i in range(5):
            queue.enqueue(f"Item {i}")
            print(f"Produced: Item {i}")
            time.sleep(0.1)
    
    def consumer():
        for i in range(5):
            try:
                item = queue.dequeue()
                print(f"Consumed: {item}")
                time.sleep(0.2)
            except IndexError:
                print("Queue is empty")
    
    # Create threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    # Start threads
    producer_thread.start()
    consumer_thread.start()
    
    # Wait for completion
    producer_thread.join()
    consumer_thread.join()
    
    print(f"Final queue state: {queue}")


if __name__ == '__main__':
    demonstrate_queue_operations()
    demonstrate_priority_queue()
    demonstrate_circular_queue()
    demonstrate_queue_applications()
    demonstrate_thread_safe_operations()

"""
Enhanced LinkedList Implementation
=================================

A comprehensive singly linked list data structure implementation with additional features:
- Basic operations (insert, delete, search)
- Advanced operations (reverse, detect cycle, find middle)
- Sorting and merging
- Utility methods
- Error handling
- Practical examples and applications

Time Complexity:
- Insert at beginning: O(1)
- Insert at end: O(n)
- Insert at position: O(n)
- Delete: O(n)
- Search: O(n)
- Access by index: O(n)
- Reverse: O(n)
- Find middle: O(n)

Space Complexity: O(n) where n is the number of nodes
"""

from typing import Any, Optional, List, Union
import random


class Node:
    """
    A node in the linked list.
    
    Attributes:
        data: The data stored in the node
        next: Reference to the next node
    """
    
    def __init__(self, data: Any = None, next_node: Optional['Node'] = None):
        """
        Initialize a node with data and next reference.
        
        Args:
            data: The data to store in the node
            next_node: Reference to the next node
        """
        self.data = data
        self.next = next_node
    
    def __str__(self) -> str:
        """String representation of the node."""
        return str(self.data)
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"Node({self.data})"


class LinkedList:
    """
    A singly linked list implementation.
    
    Attributes:
        head: Reference to the first node in the list
        size: Number of nodes in the list
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.size = 0
    
    def insert_at_beginning(self, data: Any) -> None:
        """
        Insert a new node at the beginning of the list.
        
        Args:
            data: The data to insert
        """
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1
    
    def insert_at_end(self, data: Any) -> None:
        """
        Insert a new node at the end of the list.
        
        Args:
            data: The data to insert
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def insert_at_position(self, position: int, data: Any) -> None:
        """
        Insert a new node at a specific position.
        
        Args:
            position: The position to insert at (0-based indexing)
            data: The data to insert
            
        Raises:
            IndexError: If position is invalid
        """
        if position < 0 or position > self.size:
            raise IndexError("Invalid position")
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def insert_values(self, data_list: List[Any]) -> None:
        """
        Insert multiple values from a list.
        
        Args:
            data_list: List of data to insert
        """
        self.clear()
        for data in data_list:
            self.insert_at_end(data)
    
    def delete_at_beginning(self) -> Any:
        """
        Delete the first node and return its data.
        
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If list is empty
        """
        if self.head is None:
            raise IndexError("List is empty")
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def delete_at_end(self) -> Any:
        """
        Delete the last node and return its data.
        
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If list is empty
        """
        if self.head is None:
            raise IndexError("List is empty")
        
        if self.head.next is None:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        data = current.next.data
        current.next = None
        self.size -= 1
        return data
    
    def delete_at_position(self, position: int) -> Any:
        """
        Delete a node at a specific position.
        
        Args:
            position: The position to delete from (0-based indexing)
            
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If position is invalid or list is empty
        """
        if position < 0 or position >= self.size:
            raise IndexError("Invalid position")
        
        if position == 0:
            return self.delete_at_beginning()
        
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return data
    
    def delete_by_value(self, value: Any) -> bool:
        """
        Delete the first occurrence of a value.
        
        Args:
            value: The value to delete
            
        Returns:
            True if value was found and deleted, False otherwise
        """
        if self.head is None:
            return False
        
        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, value: Any) -> int:
        """
        Search for a value and return its position.
        
        Args:
            value: The value to search for
            
        Returns:
            The position of the value (0-based), -1 if not found
        """
        current = self.head
        position = 0
        
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def contains(self, value: Any) -> bool:
        """
        Check if a value exists in the list.
        
        Args:
            value: The value to check for
            
        Returns:
            True if value exists, False otherwise
        """
        return self.search(value) != -1
    
    def get_at_position(self, position: int) -> Any:
        """
        Get the data at a specific position.
        
        Args:
            position: The position to get data from (0-based indexing)
            
        Returns:
            The data at the specified position
            
        Raises:
            IndexError: If position is invalid
        """
        if position < 0 or position >= self.size:
            raise IndexError("Invalid position")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        return current.data
    
    def set_at_position(self, position: int, value: Any) -> None:
        """
        Set the data at a specific position.
        
        Args:
            position: The position to set data at (0-based indexing)
            value: The new value
            
        Raises:
            IndexError: If position is invalid
        """
        if position < 0 or position >= self.size:
            raise IndexError("Invalid position")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        current.data = value
    
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def find_middle(self) -> Optional[Any]:
        """
        Find the middle element of the list.
        
        Returns:
            The middle element, None if list is empty
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.head is None:
            return None
        
        slow = fast = self.head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def detect_cycle(self) -> bool:
        """
        Detect if there is a cycle in the linked list.
        
        Returns:
            True if cycle exists, False otherwise
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.head is None:
            return False
        
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
    def remove_duplicates(self) -> None:
        """
        Remove duplicate elements from the list.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if self.head is None:
            return
        
        seen = set()
        current = self.head
        prev = None
        
        while current:
            if current.data in seen:
                prev.next = current.next
                self.size -= 1
            else:
                seen.add(current.data)
                prev = current
            current = current.next
    
    def sort(self) -> None:
        """
        Sort the linked list using merge sort.
        
        Time Complexity: O(n log n)
        Space Complexity: O(log n) due to recursion
        """
        self.head = self._merge_sort(self.head)
    
    def _merge_sort(self, head: Optional[Node]) -> Optional[Node]:
        """Helper method for merge sort."""
        if head is None or head.next is None:
            return head
        
        # Find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split into two halves
        second_half = slow.next
        slow.next = None
        
        # Recursively sort both halves
        left = self._merge_sort(head)
        right = self._merge_sort(second_half)
        
        # Merge sorted halves
        return self._merge(left, right)
    
    def _merge(self, left: Optional[Node], right: Optional[Node]) -> Optional[Node]:
        """Helper method to merge two sorted lists."""
        if left is None:
            return right
        if right is None:
            return left
        
        if left.data <= right.data:
            left.next = self._merge(left.next, right)
            return left
        else:
            right.next = self._merge(left, right.next)
            return right
    
    def merge_sorted(self, other: 'LinkedList') -> 'LinkedList':
        """
        Merge this list with another sorted list.
        
        Args:
            other: Another sorted linked list
            
        Returns:
            A new merged sorted linked list
        """
        result = LinkedList()
        current1 = self.head
        current2 = other.head
        
        while current1 and current2:
            if current1.data <= current2.data:
                result.insert_at_end(current1.data)
                current1 = current1.next
            else:
                result.insert_at_end(current2.data)
                current2 = current2.next
        
        # Add remaining elements
        while current1:
            result.insert_at_end(current1.data)
            current1 = current1.next
        
        while current2:
            result.insert_at_end(current2.data)
            current2 = current2.next
        
        return result
    
    def clear(self) -> None:
        """Remove all nodes from the list."""
        self.head = None
        self.size = 0
    
    def to_list(self) -> List[Any]:
        """Convert linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def get_length(self) -> int:
        """Get the number of nodes in the list."""
        return self.size
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.size == 0
    
    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        return self.size
    
    def __str__(self) -> str:
        """String representation of the linked list."""
        if self.head is None:
            return "LinkedList([])"
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return f"LinkedList([{' -> '.join(elements)}])"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return self.__str__()
    
    def __iter__(self):
        """Make the linked list iterable."""
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __getitem__(self, index: int) -> Any:
        """Support for indexing (e.g., list[0])."""
        return self.get_at_position(index)
    
    def __setitem__(self, index: int, value: Any) -> None:
        """Support for assignment (e.g., list[0] = value)."""
        self.set_at_position(index, value)


class LinkedListApplications:
    """Collection of common linked list applications and algorithms."""
    
    @staticmethod
    def add_two_numbers(l1: LinkedList, l2: LinkedList) -> LinkedList:
        """
        Add two numbers represented by linked lists.
        
        Time Complexity: O(max(n, m))
        Space Complexity: O(max(n, m))
        """
        result = LinkedList()
        carry = 0
        current1 = l1.head
        current2 = l2.head
        
        while current1 or current2 or carry:
            val1 = current1.data if current1 else 0
            val2 = current2.data if current2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            result.insert_at_end(total % 10)
            
            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next
        
        return result
    
    @staticmethod
    def is_palindrome(head: Optional[Node]) -> bool:
        """
        Check if a linked list is a palindrome.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None or head.next is None:
            return True
        
        # Find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        second_half = slow.next
        slow.next = None
        
        prev = None
        current = second_half
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Compare first and second half
        first = head
        second = prev
        
        while second:
            if first.data != second.data:
                return False
            first = first.next
            second = second.next
        
        return True
    
    @staticmethod
    def remove_nth_from_end(head: Optional[Node], n: int) -> Optional[Node]:
        """
        Remove the nth node from the end of the list.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None:
            return None
        
        # Create dummy node
        dummy = Node(0, head)
        first = second = dummy
        
        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until first reaches end
        while first:
            first = first.next
            second = second.next
        
        # Remove nth node from end
        second.next = second.next.next
        
        return dummy.next
    
    @staticmethod
    def rotate_right(head: Optional[Node], k: int) -> Optional[Node]:
        """
        Rotate the list to the right by k places.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None or head.next is None or k == 0:
            return head
        
        # Count nodes
        count = 1
        current = head
        while current.next:
            current = current.next
            count += 1
        
        # Adjust k
        k = k % count
        if k == 0:
            return head
        
        # Find new head position
        current.next = head  # Make it circular
        for _ in range(count - k):
            current = current.next
        
        new_head = current.next
        current.next = None
        
        return new_head


def demonstrate_linked_list_operations():
    """Demonstrate various linked list operations."""
    print("=== LinkedList Operations Demo ===")
    
    # Create a linked list
    ll = LinkedList()
    print(f"Created linked list: {ll}")
    print(f"Is empty: {ll.is_empty()}")
    print(f"Size: {ll.get_length()}")
    
    # Insert elements
    elements = [1, 2, 3, 4, 5]
    for elem in elements:
        ll.insert_at_end(elem)
        print(f"Inserted {elem}, List: {ll}")
    
    # Access elements
    print(f"Element at position 2: {ll.get_at_position(2)}")
    print(f"Element at position 0: {ll[0]}")  # Using indexing
    
    # Search
    print(f"Position of 3: {ll.search(3)}")
    print(f"Contains 10: {ll.contains(10)}")
    
    # Delete operations
    print(f"Deleted at beginning: {ll.delete_at_beginning()}")
    print(f"After delete at beginning: {ll}")
    
    print(f"Deleted at end: {ll.delete_at_end()}")
    print(f"After delete at end: {ll}")
    
    # Reverse
    ll.reverse()
    print(f"After reverse: {ll}")
    
    # Find middle
    print(f"Middle element: {ll.find_middle()}")
    
    # Clear
    ll.clear()
    print(f"After clear: {ll}")


def demonstrate_advanced_operations():
    """Demonstrate advanced linked list operations."""
    print("\n=== Advanced Operations Demo ===")
    
    # Create lists with duplicates
    ll1 = LinkedList()
    ll1.insert_values([1, 2, 2, 3, 4, 4, 5])
    print(f"Original list: {ll1}")
    
    # Remove duplicates
    ll1.remove_duplicates()
    print(f"After removing duplicates: {ll1}")
    
    # Sort
    ll2 = LinkedList()
    ll2.insert_values([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Unsorted list: {ll2}")
    
    ll2.sort()
    print(f"Sorted list: {ll2}")
    
    # Merge sorted lists
    ll3 = LinkedList()
    ll3.insert_values([1, 3, 5, 7])
    ll4 = LinkedList()
    ll4.insert_values([2, 4, 6, 8])
    
    merged = ll3.merge_sorted(ll4)
    print(f"Merged sorted lists: {merged}")


def demonstrate_applications():
    """Demonstrate linked list applications."""
    print("\n=== Applications Demo ===")
    
    # Add two numbers
    num1 = LinkedList()
    num1.insert_values([2, 4, 3])  # 342
    num2 = LinkedList()
    num2.insert_values([5, 6, 4])  # 465
    
    result = LinkedListApplications.add_two_numbers(num1, num2)
    print(f"Adding {num1} + {num2} = {result}")
    
    # Palindrome check
    palindrome = LinkedList()
    palindrome.insert_values([1, 2, 2, 1])
    is_pal = LinkedListApplications.is_palindrome(palindrome.head)
    print(f"Is {palindrome} a palindrome: {is_pal}")
    
    # Remove nth from end
    test_list = LinkedList()
    test_list.insert_values([1, 2, 3, 4, 5])
    print(f"Original: {test_list}")
    
    # Remove 2nd from end
    test_list.head = LinkedListApplications.remove_nth_from_end(test_list.head, 2)
    print(f"After removing 2nd from end: {test_list}")


def demonstrate_iteration():
    """Demonstrate linked list iteration."""
    print("\n=== Iteration Demo ===")
    
    ll = LinkedList()
    ll.insert_values([10, 20, 30, 40, 50])
    
    print("Iterating through the list:")
    for item in ll:
        print(f"  {item}")
    
    print("List comprehension:")
    doubled = [x * 2 for x in ll]
    print(f"  Doubled values: {doubled}")


if __name__ == '__main__':
    demonstrate_linked_list_operations()
    demonstrate_advanced_operations()
    demonstrate_applications()
    demonstrate_iteration()

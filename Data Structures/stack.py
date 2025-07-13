"""
Enhanced Stack Implementation
============================

A comprehensive stack data structure implementation with additional features:
- Basic stack operations (push, pop, peek)
- Size and empty checks
- Search functionality
- Clear operation
- String representation
- Error handling
- Practical examples and applications

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Search: O(n)
- Size: O(1)
- Empty: O(1)

Space Complexity: O(n) where n is the number of elements
"""

from collections import deque
from typing import Any, Optional, List


class Stack:
    """
    A stack implementation using deque for efficient operations.
    
    Attributes:
        container: Internal deque container for storing elements
        max_size: Maximum size limit (None for unlimited)
    """
    
    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize an empty stack.
        
        Args:
            max_size: Maximum number of elements allowed (None for unlimited)
        """
        self.container = deque()
        self.max_size = max_size
    
    def push(self, item: Any) -> bool:
        """
        Push an item onto the top of the stack.
        
        Args:
            item: The item to push onto the stack
            
        Returns:
            True if successful, False if stack is full
            
        Raises:
            OverflowError: If stack is full and max_size is set
        """
        if self.max_size is not None and len(self.container) >= self.max_size:
            raise OverflowError("Stack is full")
        
        self.container.append(item)
        return True
    
    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.container.pop()
    
    def peek(self) -> Any:
        """
        Return the top item without removing it.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.container[-1]
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.container) == 0
    
    def is_full(self) -> bool:
        """Check if the stack is full (only if max_size is set)."""
        if self.max_size is None:
            return False
        return len(self.container) >= self.max_size
    
    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.container)
    
    def clear(self) -> None:
        """Remove all items from the stack."""
        self.container.clear()
    
    def search(self, item: Any) -> int:
        """
        Find the position of an item in the stack (1-based indexing).
        
        Args:
            item: The item to search for
            
        Returns:
            Position from top (1-based), -1 if not found
        """
        try:
            # Convert to list and reverse to get top-to-bottom order
            items = list(self.container)
            items.reverse()
            return items.index(item) + 1
        except ValueError:
            return -1
    
    def contains(self, item: Any) -> bool:
        """Check if an item exists in the stack."""
        return item in self.container
    
    def to_list(self) -> List[Any]:
        """Convert stack to a list (top to bottom)."""
        return list(self.container)
    
    def __len__(self) -> int:
        """Return the number of items in the stack."""
        return len(self.container)
    
    def __str__(self) -> str:
        """String representation of the stack."""
        if self.is_empty():
            return "Stack([])"
        
        items = list(self.container)
        items.reverse()  # Show top to bottom
        return f"Stack({items})"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return self.__str__()
    
    def __bool__(self) -> bool:
        """Return True if stack is not empty."""
        return not self.is_empty()


class StackApplications:
    """Collection of common stack applications and algorithms."""
    
    @staticmethod
    def reverse_string(s: str) -> str:
        """
        Reverse a string using stack.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = Stack()
        
        # Push all characters onto stack
        for char in s:
            stack.push(char)
        
        # Pop characters to get reversed string
        result = ""
        while not stack.is_empty():
            result += stack.pop()
        
        return result
    
    @staticmethod
    def is_balanced_parentheses(s: str) -> bool:
        """
        Check if parentheses are balanced using stack.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = Stack()
        brackets = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in '({[':
                stack.push(char)
            elif char in ')}]':
                if stack.is_empty() or stack.pop() != brackets[char]:
                    return False
        
        return stack.is_empty()
    
    @staticmethod
    def evaluate_postfix(expression: str) -> int:
        """
        Evaluate postfix expression using stack.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = Stack()
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y
        }
        
        for token in expression.split():
            if token.isdigit():
                stack.push(int(token))
            elif token in operators:
                b = stack.pop()
                a = stack.pop()
                result = operators[token](a, b)
                stack.push(result)
        
        return stack.pop()
    
    @staticmethod
    def infix_to_postfix(expression: str) -> str:
        """
        Convert infix expression to postfix using stack.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = Stack()
        output = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        
        for char in expression:
            if char.isalnum():
                output.append(char)
            elif char == '(':
                stack.push(char)
            elif char == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())
                if not stack.is_empty():
                    stack.pop()  # Remove '('
            else:
                while (not stack.is_empty() and stack.peek() != '(' and
                       precedence.get(stack.peek(), 0) >= precedence.get(char, 0)):
                    output.append(stack.pop())
                stack.push(char)
        
        while not stack.is_empty():
            output.append(stack.pop())
        
        return ''.join(output)
    
    @staticmethod
    def next_greater_element(arr: List[int]) -> List[int]:
        """
        Find next greater element for each element using stack.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(arr)
        result = [-1] * n
        stack = Stack()
        
        for i in range(n):
            while not stack.is_empty() and arr[stack.peek()] < arr[i]:
                result[stack.pop()] = arr[i]
            stack.push(i)
        
        return result


def demonstrate_stack_operations():
    """Demonstrate various stack operations."""
    print("=== Stack Operations Demo ===")
    
    # Create a stack
    stack = Stack(max_size=5)
    print(f"Created stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    print(f"Size: {stack.size()}")
    
    # Push elements
    elements = [1, 2, 3, 4, 5]
    for elem in elements:
        stack.push(elem)
        print(f"Pushed {elem}, Stack: {stack}")
    
    # Try to push more (should raise error)
    try:
        stack.push(6)
    except OverflowError as e:
        print(f"Error: {e}")
    
    # Peek and pop
    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"After pop: {stack}")
    
    # Search
    print(f"Position of 3: {stack.search(3)}")
    print(f"Contains 2: {stack.contains(2)}")
    print(f"Contains 10: {stack.contains(10)}")
    
    # Clear
    stack.clear()
    print(f"After clear: {stack}")


def demonstrate_stack_applications():
    """Demonstrate stack applications."""
    print("\n=== Stack Applications Demo ===")
    
    # String reversal
    test_string = "Hello, World!"
    reversed_string = StackApplications.reverse_string(test_string)
    print(f"Original: {test_string}")
    print(f"Reversed: {reversed_string}")
    
    # Parentheses balancing
    test_cases = ["()", "({[]})", "([)]", "(((", "())"]
    for case in test_cases:
        is_balanced = StackApplications.is_balanced_parentheses(case)
        print(f"'{case}' is balanced: {is_balanced}")
    
    # Postfix evaluation
    postfix_expr = "5 3 + 2 *"
    result = StackApplications.evaluate_postfix(postfix_expr)
    print(f"Postfix '{postfix_expr}' = {result}")
    
    # Infix to postfix
    infix_expr = "a+b*c"
    postfix = StackApplications.infix_to_postfix(infix_expr)
    print(f"Infix '{infix_expr}' -> Postfix '{postfix}'")
    
    # Next greater element
    arr = [4, 5, 2, 10, 8]
    nge = StackApplications.next_greater_element(arr)
    print(f"Array: {arr}")
    print(f"Next greater elements: {nge}")


if __name__ == '__main__':
    demonstrate_stack_operations()
    demonstrate_stack_applications()

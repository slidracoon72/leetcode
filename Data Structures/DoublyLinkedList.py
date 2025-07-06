# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Define the Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Function to insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    # Function to insert a new node after a specific node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node cannot be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    # Function to insert a new node before a specific node
    def insert_before(self, next_node, data):
        if next_node is None:
            print("Next node cannot be None")
            return
        new_node = Node(data)
        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node
        if new_node.prev:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    # Function to display the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()


# Example usage
dll = DoublyLinkedList()

# Inserting nodes at the beginning
dll.insert_at_beginning(5)
dll.insert_at_beginning(3)

# Inserting node at the end
dll.insert_at_end(8)

# Inserting node after the first node
dll.insert_after(dll.head, 4)

# Inserting node before the last node
dll.insert_before(dll.head.next.next, 7)

# Display the list
dll.display()

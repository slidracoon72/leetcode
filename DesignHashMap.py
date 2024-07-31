class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


# Time: O(1), Space:O(n)
# Designing the Hash-Map as an array where index of array is the key and the element at that index is the value.
# The value is a linked list (ListNode with key, val and next).
# Neetcode: https://www.youtube.com/watch?v=cNWsgbKwwoU
class MyHashMap:
    def __init__(self):
        # Initialize a hash map with a list of ListNode objects.
        # The size of the list is 1000, and each element is a dummy node.
        self.map = [ListNode() for _ in range(1000)]

    def hash(self, key):
        # Hash function to map the key to an index in the range of the map size.
        # This is done by taking the modulus of the key with the length of the map list.
        # eg. 100 % 1000 = 100. 1100 % 100 = 100. Thus, 100 & 1100 are both stored at index 100 in the linked list
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        # Start at the head of the linked list for the computed index
        cur = self.map[self.hash(key)]  # dummy node
        # Since we have a dummy node at the beginning of the linked list, we start from the
        # next node of the current node
        while cur.next:
            # If ListNode exists
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        # If ListNode does not exist, create/insert at the last
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        # Directly point to the node after the dummy node (.next)
        cur = self.map[self.hash(key)].next
        while cur:
            # If the key is found, return its value
            if cur.key == key:
                return cur.val
            cur = cur.next
        # If the key is not found, return -1
        return -1

    def remove(self, key: int) -> None:
        # Start at the head of the linked list for the computed index
        cur = self.map[self.hash(key)]
        # Traverse the linked list to find the key
        while cur and cur.next:
            # If the key is found, remove the node by updating the pointer
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

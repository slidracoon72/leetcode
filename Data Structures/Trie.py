from typing import List, Dict, Optional


class TrieNode:
    """
    Node class for Trie data structure.
    Each node contains:
    - children: Dictionary mapping characters to child nodes
    - is_end_of_word: Boolean indicating if this node marks the end of a word
    - word_count: Number of words that end at this node
    """
    
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.word_count: int = 0


class Trie:
    """
    Trie (Prefix Tree) implementation with comprehensive functionality.
    
    A Trie is a tree-like data structure used to store and retrieve strings.
    It's particularly useful for:
    - Autocomplete functionality
    - Spell checking
    - IP routing tables
    - Dictionary implementations
    
    Time Complexity for most operations: O(m) where m is the length of the string
    Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of keys, M is average key length
    """
    
    def __init__(self):
        """Initialize an empty Trie with a root node."""
        self.root = TrieNode()
        self.total_words = 0
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.
        
        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(m) for new nodes created
        
        Args:
            word: The word to insert into the Trie
        """
        if not word:
            return
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        
        # Mark the end of the word
        if not current.is_end_of_word:
            current.is_end_of_word = True
            self.total_words += 1
        current.word_count += 1
    
    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.
        
        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(1)
        
        Args:
            word: The word to search for
            
        Returns:
            True if the word exists in the Trie, False otherwise
        """
        if not word:
            return False
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return current.is_end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in the Trie starts with the given prefix.
        
        Time Complexity: O(m) where m is the length of the prefix
        Space Complexity: O(1)
        
        Args:
            prefix: The prefix to search for
            
        Returns:
            True if any word starts with the prefix, False otherwise
        """
        if not prefix:
            return True
        
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return True
    
    def delete(self, word: str) -> bool:
        """
        Delete a word from the Trie.
        
        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(1)
        
        Args:
            word: The word to delete
            
        Returns:
            True if the word was deleted, False if it didn't exist
        """
        if not word:
            return False
        
        def delete_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    node.word_count -= 1
                    self.total_words -= 1
                    return True
                return False
            
            char = word[index]
            if char not in node.children:
                return False
            
            should_delete_child = delete_helper(node.children[char], word, index + 1)
            
            if should_delete_child and not node.children[char].is_end_of_word and not node.children[char].children:
                del node.children[char]
                return True
            
            return False
        
        return delete_helper(self.root, word, 0)
    
    def get_all_words(self) -> List[str]:
        """
        Get all words stored in the Trie.
        
        Time Complexity: O(N * M) where N is number of words, M is average word length
        Space Complexity: O(N * M) for storing all words
        
        Returns:
            List of all words in the Trie
        """
        words = []
        
        def collect_words(node: TrieNode, current_word: str):
            if node.is_end_of_word:
                words.append(current_word)
            
            for char, child in node.children.items():
                collect_words(child, current_word + char)
        
        collect_words(self.root, "")
        return words
    
    def get_words_with_prefix(self, prefix: str) -> List[str]:
        """
        Get all words that start with the given prefix.
        
        Time Complexity: O(m + k) where m is prefix length, k is number of words with prefix
        Space Complexity: O(k * M) where k is number of words, M is average word length
        
        Args:
            prefix: The prefix to search for
            
        Returns:
            List of words that start with the prefix
        """
        if not prefix:
            return self.get_all_words()
        
        words = []
        
        # Navigate to the node representing the prefix
        current = self.root
        for char in prefix:
            if char not in current.children:
                return words
            current = current.children[char]
        
        # Collect all words from this node
        def collect_words_from_node(node: TrieNode, current_word: str):
            if node.is_end_of_word:
                words.append(current_word)
            
            for char, child in node.children.items():
                collect_words_from_node(child, current_word + char)
        
        collect_words_from_node(current, prefix)
        return words
    
    def get_word_count(self, word: str) -> int:
        """
        Get the count of how many times a word appears in the Trie.
        
        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(1)
        
        Args:
            word: The word to count
            
        Returns:
            Number of times the word appears in the Trie
        """
        if not word:
            return 0
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                return 0
            current = current.children[char]
        
        return current.word_count if current.is_end_of_word else 0
    
    def get_longest_common_prefix(self) -> str:
        """
        Find the longest common prefix among all words in the Trie.
        
        Time Complexity: O(N * M) where N is number of words, M is average word length
        Space Complexity: O(M) for the result string
        
        Returns:
            The longest common prefix
        """
        if not self.root.children:
            return ""
        
        prefix = ""
        current = self.root
        
        # Continue until we find a node with more than one child or end of word
        while len(current.children) == 1 and not current.is_end_of_word:
            char = next(iter(current.children.keys()))
            prefix += char
            current = current.children[char]
        
        return prefix
    
    def get_size(self) -> int:
        """
        Get the total number of words in the Trie.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Returns:
            Total number of words
        """
        return self.total_words
    
    def is_empty(self) -> bool:
        """
        Check if the Trie is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Returns:
            True if Trie is empty, False otherwise
        """
        return self.total_words == 0
    
    def clear(self) -> None:
        """
        Remove all words from the Trie.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.root = TrieNode()
        self.total_words = 0


class WordDictionary:
    """
    Word Dictionary with wildcard support (like LeetCode 211).
    Supports '.' as a wildcard character that can match any single character.
    """
    
    def __init__(self):
        """Initialize an empty Word Dictionary."""
        self.trie = Trie()
    
    def add_word(self, word: str) -> None:
        """
        Add a word to the dictionary.
        
        Args:
            word: The word to add
        """
        self.trie.insert(word)
    
    def search(self, word: str) -> bool:
        """
        Search for a word in the dictionary.
        Supports '.' as a wildcard character.
        
        Time Complexity: O(26^m) in worst case where m is word length (due to wildcards)
        Space Complexity: O(m) for recursion stack
        
        Args:
            word: The word to search for (can contain '.' wildcards)
            
        Returns:
            True if the word exists, False otherwise
        """
        if not word:
            return False
        
        def search_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                return node.is_end_of_word
            
            char = word[index]
            
            if char == '.':
                # Try all possible characters
                for child in node.children.values():
                    if search_helper(child, word, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return search_helper(node.children[char], word, index + 1)
        
        return search_helper(self.trie.root, word, 0)


# Example usage and testing
if __name__ == "__main__":
    print("Trie Data Structure Demo:")
    print("========================")
    
    # Basic Trie operations
    trie = Trie()
    
    # Insert words
    words = ["apple", "app", "application", "banana", "band", "bandana"]
    for word in words:
        trie.insert(word)
        print(f"Inserted: {word}")
    
    print(f"\nTotal words in Trie: {trie.get_size()}")
    
    # Search operations
    search_words = ["apple", "app", "banana", "orange", "band"]
    for word in search_words:
        exists = trie.search(word)
        print(f"Search '{word}': {exists}")
    
    # Prefix operations
    prefixes = ["app", "ban", "or"]
    for prefix in prefixes:
        starts_with = trie.starts_with(prefix)
        words_with_prefix = trie.get_words_with_prefix(prefix)
        print(f"Words starting with '{prefix}': {words_with_prefix}")
    
    # Get all words
    all_words = trie.get_all_words()
    print(f"\nAll words in Trie: {all_words}")
    
    # Longest common prefix
    lcp = trie.get_longest_common_prefix()
    print(f"Longest common prefix: '{lcp}'")
    
    # Delete operation
    print(f"\nDeleting 'app': {trie.delete('app')}")
    print(f"Search 'app' after deletion: {trie.search('app')}")
    print(f"Search 'apple' after deletion: {trie.search('apple')}")
    
    # Word Dictionary with wildcards
    print("\n" + "="*50)
    print("Word Dictionary with Wildcards Demo:")
    print("="*50)
    
    word_dict = WordDictionary()
    word_dict.add_word("bad")
    word_dict.add_word("dad")
    word_dict.add_word("mad")
    
    test_searches = ["pad", "bad", ".ad", "b.."]
    for search in test_searches:
        result = word_dict.search(search)
        print(f"Search '{search}': {result}")
    
    # Multiple insertions of same word
    print("\n" + "="*50)
    print("Multiple Insertions Demo:")
    print("="*50)
    
    trie2 = Trie()
    trie2.insert("hello")
    trie2.insert("hello")
    trie2.insert("hello")
    
    print(f"Count of 'hello': {trie2.get_word_count('hello')}")
    print(f"Count of 'world': {trie2.get_word_count('world')}")
    
    # Clear operation
    trie2.clear()
    print(f"Trie empty after clear: {trie2.is_empty()}") 
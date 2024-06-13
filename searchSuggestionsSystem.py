from typing import List


# Solving using two-pointers
# Neetcode: https://www.youtube.com/watch?v=D4T2N0yAr20
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Initialize an empty list to store the suggested products for each prefix
        res = []

        # Sort the products list in lexicographical order
        products.sort()

        # Initialize two pointers, l and r, to the start and end of the products list
        l, r = 0, len(products) - 1

        # Iterate over each character in the searchWord
        for i in range(len(searchWord)):
            c = searchWord[i]

            # Move the left pointer (l) to the first product that starts with the current prefix
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1

            # Move the right pointer (r) to the last product that starts with the current prefix
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            # Create a new sublist in res to store the suggested products for the current prefix
            res.append([])

            # Calculate the number of products that start with the current prefix
            window = r - l + 1

            # Add the first three products (or fewer if there are less than three) that start with the current prefix
            # to the sublist
            for j in range(min(3, window)):
                res[-1].append(products[l + j])

        # Return the list of suggested products for each prefix
        return res


# Solving using Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

            # Store the word at each node
            node.words.append(word)
            # Keep only the first 3 lexicographically minimum words
            node.words.sort()
            node.words = node.words[:3]

    def search(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        return node.words


class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        res = []

        for product in products:
            trie.insert(product)

        prefix = ''
        for p in searchWord:
            prefix += p
            # Search for products with current prefix
            suggestions = trie.search(prefix)
            res.append(suggestions)

        return res


#
# node.words.sort()
#           node.words = node.words[:3]

l = ["mouse"]
print(l[:3])

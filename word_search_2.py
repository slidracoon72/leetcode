from typing import List


# Neetcode: https://www.youtube.com/watch?v=asbcE9mZz_U
class TrieNode:
    def __init__(self):
        """
        Initializes a TrieNode object.
        """
        self.children = {}  # Dictionary to store children nodes
        self.endOfWord = {}  # Flag to indicate the end of a word

    def addWord(self, word: str):
        """
        Adds a word to the trie.

        Args:
            word (str): The word to be added.
        """
        cur = self

        # Traverse through each character of the word
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()  # Create a new node if character not present
            cur = cur.children[c]
        cur.endOfWord = True  # Mark the end of the word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Finds the words present on the board.

        Args:
            board (List[List[str]]): The board containing characters.
            words (List[str]): The list of words to find.

        Returns:
            List[str]: List of words found on the board.
        """
        # Initialize the root node of the trie
        root = TrieNode()

        # Add each word to the trie
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, path = set(), set()

        def dfs(r, c, node, word):
            """
            Performs depth-first search to traverse the board and find words.

            Args:
                r (int): Row index.
                c (int): Column index.
                node (TrieNode): Current node in the trie.
                word (str): Word formed so far.
            """
            # Check if the indices are out of bounds or if the current position has already been visited,
            # or if the character at the current position is not a child of the current node
            if (r < 0 or c < 0 or r == ROWS or
                    c == COLS or (r, c) in path or
                    board[r][c] not in node.children):
                return

            # Mark the current position as visited
            path.add((r, c))

            # Move to the child node corresponding to the character at the current position
            node = node.children[board[r][c]]
            word += board[r][c]  # Update the word formed so far

            # If the current node marks the end of a word, add it to the result set
            if node.endOfWord:
                res.add(word)

            # Explore neighboring cells recursively
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Remove the current position from the visited set to backtrack
            path.remove((r, c))

        # Iterate through each cell in the board and perform DFS
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

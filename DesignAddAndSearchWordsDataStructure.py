# Neetcode: https://www.youtube.com/watch?v=BTf05gs_8iU
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str, node=None) -> bool:
        if node is None:
            node = self.root

        for i, c in enumerate(word):
            if c == '.':
                for child in node.children.values():
                    if self.search(word[i + 1:], child):
                        return True
                return False
            elif c not in node.children:
                return False
            node = node.children[c]

        return node.endOfWord

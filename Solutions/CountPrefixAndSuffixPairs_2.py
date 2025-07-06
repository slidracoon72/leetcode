# LC - Hard

from typing import List


# Solved using Trie - Combined both Prefix and Suffix Trees
# Neetcode: https://www.youtube.com/watch?v=zQrtsvo8lgM
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        cur = self.root

        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in cur.children:
                cur.children[(c1, c2)] = TrieNode()
            cur = cur.children[(c1, c2)]
            cur.count += 1

    def count(self, w):
        cur = self.root

        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in cur.children:
                return 0
            cur = cur.children[(c1, c2)]
        return cur.count


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        root = Trie()

        for w in reversed(words):
            res += root.count(w)
            root.add(w)

        return res


c = Solution()
words = ["a", "aba", "ababa", "aa"]
print(c.countPrefixSuffixPairs(words))

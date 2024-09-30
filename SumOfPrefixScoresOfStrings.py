# LC-Hard


from collections import defaultdict
from typing import List


class Solution:
    # Using HashSet
    # Time Complexity: O(n * L), where n is the number of words and L is the average length of words.
    # Space Complexity: O(n * L), for storing the prefix counts and the result array.
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # List to store the final scores for each word
        res = []
        # Dictionary to count how many times each prefix appears across all words
        count = defaultdict(int)

        # First pass: Count the occurrences of every prefix in all words
        for w in words:
            # For each word, we generate all prefixes and update their counts
            for i in range(len(w)):
                prefix = w[:i + 1]  # Extract the prefix from the word
                count[prefix] += 1  # Increment the count for this prefix

        # Second pass: Calculate the prefix score for each word
        for w in words:
            score = 0  # Initialize the score for the current word
            # For each word, sum the scores of all its prefixes
            for i in range(len(w)):
                prefix = w[:i + 1]  # Extract the prefix from the word
                score += count[prefix]  # Add the count of the current prefix to the score
            res.append(score)  # Store the score in the result list

        return res  # Return the list of scores for all words


#########################
# Neetcode: https://www.youtube.com/watch?v=F-5cmvhLw90
# Using Prefix Tree (Trie Data Structure)
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
            cur.count += 1

    def get_score(self, word):
        cur = self.root
        score = 0
        for c in word:
            i = ord(c) - ord('a')
            cur = cur.children[i]
            score += cur.count
        return score


class Solution2:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        prefix_tree = Trie()
        for word in words:
            prefix_tree.insert(word)

        for word in words:
            score = prefix_tree.get_score(word)
            res.append(score)

        return res

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a mapping of each character to its index in the alien dictionary
        order_index = {c: i for i, c in enumerate(order)}

        # Helper function to convert a word into a list of indices based on the alien order
        def compare(word):
            # Each character in the word is replaced with its alien order index
            return [order_index[c] for c in word]

        # Compare the original list of words with the list sorted using alien order
        # If they are equal, the words are sorted correctly in alien language
        return words == sorted(words, key=compare)


c = Solution()
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(c.isAlienSorted(words, order))

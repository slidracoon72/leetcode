from typing import List


class Solution:
    # Greedy Solution
    # Time: O(n), Space: O(n)
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)  # Get the number of words

        res = [words[0]]  # List to store the result subsequence. Always include the first word

        prev = groups[0]  # Initialize the previous group with the first group's value

        # Iterate through the words starting from the second word
        for i in range(1, n):
            w = words[i]  # Current word
            g = groups[i]  # Current group number

            # Only add the word to the result if its group is different from the previous one
            if prev != g:
                res.append(w)  # Add word to result
                prev = g  # Update previous group to current group

        return res  # Return the longest alternating group subsequence of words


c = Solution()
words = ["e", "a", "b"]
groups = [0, 0, 1]
print(c.getLongestSubsequence(words, groups))

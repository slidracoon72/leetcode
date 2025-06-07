# LC-2434: Using a Robot to Print the Lexicographically Smallest String

from collections import Counter


class Solution:
    # Solved using Greedy + Stack
    # Time: O(n), Space: O(n)
    def robotWithString(self, s: str) -> str:
        # Count how many times each character appears in the string
        cnt = Counter(s)

        res = []  # Final result string 'p' — built by popping from stack
        stack = []  # Temporary stack 't' — characters are pushed here before moving to 'p'
        min_ch = 'a'  # Tracks the smallest character still available in the remaining input

        for ch in s:
            # Always push the current character to the stack
            stack.append(ch)
            # Decrease the frequency count since we've now processed this character
            cnt[ch] -= 1

            # Update min_ch to point to the next smallest character still left in the input
            while min_ch <= 'z' and cnt[min_ch] == 0:
                min_ch = chr(ord(min_ch) + 1)

            # While the top of the stack is <= the smallest character left in the input,
            # pop from stack to result (this maintains lexicographical order)
            while stack and stack[-1] <= min_ch:
                res.append(stack.pop())

        return ''.join(res)

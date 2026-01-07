from typing import List


class Solution:
    # Similar to Subsets.py
    # Time: O(n * 2^n + m), Space: O(n * 2^n); where n = len(s) and m = len(words)
    def count_subsequences_from_a_word(self, s: str, words: List[str]) -> int:
        res = set()

        def dfs(i, cur):
            if i == len(s):
                res.add("".join(cur))
                return

            # include
            cur.append(s[i])
            dfs(i + 1, cur)
            # skip
            cur.pop()
            dfs(i + 1, cur)

        dfs(0, [])

        count = 0
        for word in words:
            if word in res:
                count += 1

        return count


c = Solution()
s = "abcde"
words = ["a", "bb", "acd", "ace"]
print(c.count_subsequences_from_a_word(s, words))

s = "dsahjpjauf"
words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
print(c.count_subsequences_from_a_word(s, words))

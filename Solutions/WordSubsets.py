from collections import Counter
from typing import List


class Solution:
    # Brute Force - Gives TLE
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        for word in words1:
            c = Counter(word)
            flag = True
            for sub in words2:
                s = Counter(sub)
                for ch in s:
                    if s[ch] > c[ch]:
                        flag = False
                        break
            if flag:
                res.append(word)

        return res

    # Optimized from brute force solution
    # Time: O(n+m), Space: O(n+m)
    def wordSubsets1(self, words1: List[str], words2: List[str]) -> List[str]:
        # Calculate the maximum frequency of each character required by all words in words2
        max_freq = Counter()
        for sub in words2:
            sub_counter = Counter(sub)
            for ch, count in sub_counter.items():
                max_freq[ch] = max(max_freq[ch], count)

        # Check each word in words1 to see if it meets the universal condition
        res = []
        for word in words1:
            word_counter = Counter(word)
            if all(word_counter[ch] >= count for ch, count in max_freq.items()):
                res.append(word)

        return res

    # Incorrect logic applied
    def wordSubsets2(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        for word in words1:
            flag = True
            for sub in words2:
                i, j = 0, 0
                while i < len(word) and j < len(sub):
                    if word[i] == sub[j]:
                        j += 1
                    i += 1
                if j != len(sub):
                    flag = False
                    break
            if flag:
                res.append(word)

        return res


c = Solution()
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["lc", "eo"]
print(c.wordSubsets1(words1, words2))

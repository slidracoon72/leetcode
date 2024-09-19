from typing import List, Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Combine both sentences and count occurrences of all words
        count = Counter((s1 + " " + s2).split())

        # Return words that appear exactly once across both sentences
        res = []
        for word, freq in count.items():
            if freq == 1:
                res.append(word)
        return res

        # Can also use list comprehension
        # return [word for word, freq in count.items() if freq == 1]

    # Less Optimal
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = Counter(s1.split(" "))
        c2 = Counter(s2.split(" "))
        res = []
        for w in c1:
            if c1[w] == 1 and w not in c2:
                res.append(w)
        for w in c2:
            if c2[w] == 1 and w not in c1:
                res.append(w)
        return res

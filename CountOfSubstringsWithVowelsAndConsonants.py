# LC-3305 Count of Substrings Containing Every Vowel and K Consonants I
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(word)
        res = 0

        for l in range(n):
            c = 0
            seen = set()
            for r in range(l, n):
                cur = word[r]
                if cur in vowels:
                    seen.add(cur)
                else:
                    c += 1
                    if c > k:
                        break
                if c == k and seen == vowels:
                    res += 1

        return res

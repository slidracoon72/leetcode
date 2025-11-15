from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # A set for exact matches (case-sensitive)
        seen = set(wordlist)

        # Dictionary for case-insensitive matches: maps lowercase word -> original word
        caps = {}

        # Dictionary for vowel-error matches: maps "normalized" word (vowels replaced with *) -> original word
        vows = {}

        # Helper function to normalize a word by replacing vowels with '*'
        def norm(w):
            ans = []
            for c in w.lower():  # convert to lowercase
                if c in "aeiou":  # check if character is a vowel
                    ans.append("*")  # replace vowel with '*'
                else:
                    ans.append(c)  # keep consonants as they are
            return "".join(ans)  # return the normalized string

        # Populate caps and vows dictionaries using reversed wordlist
        # Reversing ensures that the FIRST occurrence in wordlist is preserved (later words overwrite earlier ones)
        for word in reversed(wordlist):
            caps[word.lower()] = word  # store lowercase -> original word for case-insensitive match
            vows[norm(word)] = word  # store normalized -> original word for vowel match

        res = []  # list to store results for each query

        # Process each query
        for q in queries:
            # 1. Exact match (case-sensitive)
            if q in seen:
                res.append(q)
                continue

            # 2. Case-insensitive match
            if q.lower() in caps:
                res.append(caps[q.lower()])
                continue

            # 3. Vowel-error match (normalized form)
            vnorm = norm(q)
            if vnorm in vows:
                res.append(vows[vnorm])
                continue

            # 4. No match found
            res.append("")

        return res


c = Solution()
wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
print(c.spellchecker(wordlist, queries))

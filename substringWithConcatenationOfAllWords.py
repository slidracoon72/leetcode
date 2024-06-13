from collections import Counter
from typing import List


# Sliding Window - Hard
# Youtube: https://www.youtube.com/watch?v=taYRJf-M25I
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        total_length = len(words) * word_length
        result = []

        words_count = Counter(words)

        for i in range(len(s) - total_length + 1):
            substr = s[i:i + total_length]
            substr_words = []
            for j in range(0, total_length, word_length):
                substr_words.append(substr[j:j + word_length])
            substr_count = Counter(substr_words)
            if substr_count == words_count:
                result.append(i)

        return result


c = Solution()
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(c.findSubstring(s1, words1))

s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(c.findSubstring(s2, words2))

s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
print(c.findSubstring(s3, words3))

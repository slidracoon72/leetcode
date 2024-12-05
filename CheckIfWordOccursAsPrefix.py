# LC 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if word[:len(searchWord)] == searchWord:
                return i + 1
        return -1

    # Solved using startswith(), similar as above
    def isPrefixOfWord1(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1


c = Solution()
sentence = "i love eating burger"
searchWord = "burg"
print(c.isPrefixOfWord(sentence, searchWord))

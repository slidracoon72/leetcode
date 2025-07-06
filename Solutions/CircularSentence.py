class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()

        if s[0][0] != s[-1][-1]:
            return False

        for i in range(len(s) - 1):
            if s[i][-1] != s[i + 1][0]:
                return False

        return True

    def isCircularSentence1(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False

        i = 0
        while i < (len(sentence) - 1):
            if sentence[i] == ' ':
                if sentence[i - 1] != sentence[i + 1]:
                    return False
            i += 1

        return True

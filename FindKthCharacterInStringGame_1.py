class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        res = ''

        while len(res) < k:
            res += word
            word_list = list(res)
            for i in range(len(word_list)):
                word_list[i] = chr(ord(word_list[i]) + 1)
            word = "".join(word_list)

        return res[k - 1]

    def kthCharacter1(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            temp = ""
            for x in word:
                temp += chr(ord('a') + ((ord(x) - ord('a')) + 1) % 26)
            word += temp

        return word[k - 1]


c = Solution()
print(c.kthCharacter1(5))
print(c.kthCharacter1(10))

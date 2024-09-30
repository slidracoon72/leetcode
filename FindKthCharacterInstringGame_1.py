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

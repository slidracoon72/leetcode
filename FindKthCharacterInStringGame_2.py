# LC - Hard
# DO AGAIN

from typing import List


class Solution:
    # Getting TLE - 732 / 901 testcases passed
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        word = "a"
        for o in operations:
            if o == 0:
                word += word
            else:
                temp = ""
                for x in word:
                    temp += chr(ord('a') + ((ord(x) - ord('a')) + 1) % 26)
                word += temp

        return word[k - 1]

    def kthCharacter1(self, k: int, operations: List[int]) -> str:
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]:
                ans += 1
        return chr(ord("a") + (ans % 26))

# LC-1945: Sum of Digits of String After Convert
class Solution:
    # Time: O(k * n), Space: O(n)
    def getLucky(self, s: str, k: int) -> int:
        # convert
        temp = ""
        for c in s:
            temp += str((ord(c) - ord("a")) + 1)

        # transform
        while k > 0:
            res = 0
            for c in temp:
                res += int(c)
            k -= 1
            temp = str(res)
        return res


c = Solution()
s = "leetcode"
k = 2
print(c.getLucky(s, k))

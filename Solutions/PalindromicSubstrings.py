# Neetcode: https://www.youtube.com/watch?v=4RACzI5-du8
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # odd length substrings
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            # even length substrings
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count


# Same code, but optimized
class Solution2:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # for odd expansions
            res += self.countPali(s, i, i)
            # for even expansions
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res


c = Solution()
s = "aaa"
print(c.countSubstrings(s))

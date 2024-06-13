class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        t = list(t)
        d = dict()
        if len(s) != len(t) or len(set(s)) != len(set(t)): return False
        for i, c in enumerate(s):
            if c in d:
                if d[c] != t[i]: return False
            else:
                d[c] = t[i]
        return True


v = Solution()
s = "badc"
t = "baba"

print(v.isIsomorphic(s, t))

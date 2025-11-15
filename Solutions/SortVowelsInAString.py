class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        res = list(s)

        temp = []
        for i, c in enumerate(s):
            if c in vowels:
                asc = ord(c)
                temp.append((asc, i, c))

        temp.sort()
        v = []
        o = []
        for _, i, c in temp:
            v.append(c)
            o.append(i)
        v.sort()
        o.sort()

        for i in range(len(v)):
            res[o[i]] = v[i]

        return "".join(res)

    # Optimized Solution
    # Time: O(nlogn), Space: O(n)
    def sortVowels1(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        temp = sorted(s)

        v = []
        for c in temp:
            if c in vowels:
                v.append(c)

        j, l = 0, len(temp)
        res = list(s)
        for i, c in enumerate(res):
            if c in vowels:
                res[i] = v[j]
                j += 1
                if j == l:
                    break

        return "".join(res)


c = Solution()
print(c.sortVowels("lEetcOde"))
print(c.sortVowels1("lEetcOde"))
print(c.sortVowels("lYmpH"))
print(c.sortVowels1("lYmpH"))

class Solution:
    def makeFancyString(self, s: str) -> str:
        # Initialize result with the first character and a counter for consecutive characters
        result = [s[0]]
        count = 1

        # Iterate from the second character onward
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1  # Reset count if current character is different

            # Only add the character if it doesn't result in three consecutive identical characters
            if count < 3:
                result.append(s[i])

        return ''.join(result)

    def makeFancyString1(self, s: str) -> str:
        s_list = list(s)
        ind = set()

        for i in range(len(s) - 2):
            if s_list[i] == s_list[i + 1] == s_list[i + 2]:
                ind.add(i)

        if not ind:
            return s

        res = ""
        for i in range(len(s)):
            if i not in ind:
                res += s[i]
        return res

    def makeFancyString2(self, s: str) -> str:
        n = len(s)
        if n <= 2:
            return s

        remove = set()

        i, j, k = 0, 1, 2
        while k < n:
            if s[i] == s[j] == s[k]:
                remove.add(i)
            i, j, k = i + 1, j + 1, k + 1

        if not remove:
            return s

        res = ""
        for i in range(n):
            if i not in remove:
                res += s[i]

        return res


c = Solution()
s = "leeetcode"
print(c.makeFancyString2(s))

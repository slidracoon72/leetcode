class Solution:
    def maximum69Number(self, num: int) -> int:
        n = list(str(num))
        for i in range(len(n)):
            if n[i] != "9":
                n[i] = "9"
                break
        return int(''.join(n))


c = Solution()
print(c.maximum69Number(9669))
print(c.maximum69Number(9996))
print(c.maximum69Number(6666))

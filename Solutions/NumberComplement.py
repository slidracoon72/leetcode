class Solution:
    def findComplement(self, num: int) -> int:
        b = list(bin(num)[2:])

        for i in range(len(b)):
            if b[i] == '0':
                b[i] = '1'
            else:
                b[i] = '0'
        b = "".join(b)

        return int(b, 2)


c = Solution()
num = 5
print(c.findComplement(num))

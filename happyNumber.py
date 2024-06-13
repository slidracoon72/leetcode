class Solution:
    def isHappy(self, n: int) -> bool:
        l = []
        while n not in l:
            l.append(n)
            digits = list(str(n))
            temp = 0
            for digit in digits:
                temp += int(digit) ** 2
            if temp == 1:
                return True
            n = temp
        return False


obj = Solution()
print(obj.isHappy(2))
print(obj.isHappy(7))
print(obj.isHappy(19))

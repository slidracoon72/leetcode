class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n > 1:
            digits = str(n)
            temp = 0
            for d in digits:
                temp += int(d) ** 2
            if temp in visit:
                return False
            visit.add(temp)
            n = temp

        return True


obj = Solution()
print(obj.isHappy(2))
print(obj.isHappy(7))
print(obj.isHappy(19))

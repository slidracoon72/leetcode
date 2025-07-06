from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                l.insert(i, "FizzBuzz")
            elif i % 3 == 0:
                l.insert(i, "Fizz")
            elif i % 5 == 0:
                l.insert(i, "Buzz")
            else:
                l.append(str(i))
        return l

    def fizzBuzz1(self, n: int) -> List[str]:
        return [str(i) * (i % 3 != 0 and i % 5 != 0) + "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)
                for i in range(1, n + 1)]


c = Solution()
print(c.fizzBuzz(3))
print(c.fizzBuzz1(3))
print("--------------")
print(c.fizzBuzz(5))
print(c.fizzBuzz1(5))
print("--------------")
print(c.fizzBuzz(15))
print(c.fizzBuzz1(15))
print("--------------")

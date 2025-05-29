class Solution:
    # Time: O(n), Space: O(1)
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0

        for i in range(1, n + 1):
            # If not divisible, add to num1
            if i % m:
                num1 += i
            # If divisible, add to num2
            else:
                num2 += i

        return num1 - num2


c = Solution()
print(c.differenceOfSums(10, 3))

from collections import defaultdict, Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n <= 9:
            return n

        def sum_of_digits(n: int) -> int:
            n = str(n)
            num = 0
            for x in n:
                num += int(x)
            return num

        numSum = defaultdict(int)
        for num in range(1, n + 1):
            s = sum_of_digits(num)
            numSum[s] += 1

        groups = Counter(numSum.values())
        return groups[max(groups)]


c = Solution()
print(c.countLargestGroup(13))
print(c.countLargestGroup(2))
print(c.countLargestGroup(16))

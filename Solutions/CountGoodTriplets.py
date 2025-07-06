from typing import List


class Solution:
    # Brute Force
    # Time: O(n^3), Space: O(1)
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1
        return res


sol = Solution()
arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
print(sol.countGoodTriplets(arr, a, b, c))

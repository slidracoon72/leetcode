from collections import Counter, defaultdict
from typing import List


# Neetcode: https://www.youtube.com/watch?v=1KOnvGPv9Mo
class Solution:
    # Time: O(n), Space: O(n)
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        res = []

        for x in arr:
            if count[x] == 1 and x not in res:
                res.append(x)

        return res[k - 1] if not len(res) < k else ""

    # Time: O(n), Space: O(n)
    # Best Solution of all three
    def kthDistinct1(self, arr: List[str], k: int) -> str:
        count = defaultdict(int)
        for s in arr:
            count[s] += 1
        for s in arr:
            if count[s] == 1:
                k -= 1
            if k == 0:
                return s
        return ""

    # Time: O(n^2), Space: O(1)
    def kthDistinct2(self, arr: List[str], k: int) -> str:
        for i in range(len(arr)):
            distinct_flag = True
            for j in range(len(arr)):
                # to avoid comparing the same element
                if i == j:
                    continue
                if arr[i] == arr[j]:
                    distinct_flag = False
                    break
            if distinct_flag:
                k -= 1
                if k == 0:
                    return arr[i]
        return ""


c = Solution()
arr = ["d", "b", "c", "b", "c", "a"]
# arr = ["aaa", "aa", "a"]
k = 2
print(c.kthDistinct(arr, k))

from typing import List


class Solution:
    # Sliding Window
    # Time: O(1), Space: O(1)
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res, prev = 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""

        return res


c = Solution()
arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
print(c.maxTurbulenceSize(arr))

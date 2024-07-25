# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time
# complexity and with the smallest space complexity possible.

from typing import List


class Solution:
    # Using Merge Sort
    # Time: O(nlogn), Space: O(n)
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.sortArray(arr[:mid])
        right = self.sortArray(arr[mid:])

        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


c = Solution()
arr = [5, 2, 3, 1]
print(c.sortArray(arr))

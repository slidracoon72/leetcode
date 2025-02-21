from typing import List


# Solved using Binary Search (Two-Pointers)
# Time: O(logn), Space: O(logn)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, f = 0, len(numbers) - 1
        while s < f:
            temp = numbers[s] + numbers[f]
            if temp == target:
                return [s + 1, f + 1]
            elif temp < target:
                s += 1
            else:
                f -= 1
        return []

    def twoSum_alternate(self, numbers: List[int], target: int) -> List[int]:
        s, f = 0, 1
        while f < len(numbers):
            temp = numbers[s] + numbers[f]
            if temp == target:
                return [s + 1, f + 1]
            elif temp < target:
                f += 1
            else:
                s += 1
                f = s + 1
        return []  # Return empty list if no such pair is found


c = Solution()
numbers = [3, 24, 50, 79, 88, 150, 345]
target = 200
print(c.twoSum(numbers, target))
print(c.twoSum_alternate(numbers, target))

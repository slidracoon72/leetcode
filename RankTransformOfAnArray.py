from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        sorted_arr = sorted(arr)
        d = {}
        rank = 0
        d[sorted_arr[0]] = rank
        for i in range(1, len(sorted_arr)):
            if sorted_arr[i - 1] != sorted_arr[i]:
                rank += 1
            d[sorted_arr[i]] = rank

        res = []
        for x in arr:
            res.append(d[x] + 1)
        return res

    # Similar Approach, Optimized code
    # Time: O(nlogn), Space: O(n)
    def arrayRankTransform1(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        # Create a sorted version of arr without duplicates
        sorted_arr = sorted(set(arr))

        # Create a dictionary that maps each element to its rank (1-based)
        d = {x: i + 1 for i, x in enumerate(sorted_arr)}

        # Return the rank of each element in the original array
        return [d[x] for x in arr]

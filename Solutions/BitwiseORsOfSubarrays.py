from typing import List


class Solution:
    # Brute Force - Gives TLE (77 / 85 testcases passed)
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        res = set()
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur |= arr[j]
                res.add(cur)

        return len(res)

    # Frontier Set
    def subarrayBitwiseORs1(self, arr: List[int]) -> int:
        res = set()  # To store all unique results of subarray ORs
        cur = {0}  # Set of OR values for subarrays ending at the previous index

        for x in arr:
            # For each number, compute new ORs by combining with all previous ORs
            cur = {x | y for y in cur} | {x}
            res |= cur  # Add current OR results to the final result set

        return len(res)  # Return the count of unique OR values

    # Similar as above - Expanded for better understanding
    def subarrayBitwiseORs2(self, arr: List[int]) -> int:
        all_or_results = set()  # Set to store all unique OR results
        prev_or_set = set([0])  # Stores OR results of subarrays ending at previous index

        for num in arr:
            # Compute new OR results ending at current element
            curr_or_set = {num}  # Start with the number itself

            for prev in prev_or_set:
                curr_or_set.add(prev | num)  # Combine with all previous ORs

            # Add current OR results to the final set
            all_or_results.update(curr_or_set)

            # Update the previous OR set for next iteration
            prev_or_set = curr_or_set

        return len(all_or_results)  # Total number of distinct OR values


c = Solution()
arr = [1, 2, 4]
print(c.subarrayBitwiseORs2(arr))

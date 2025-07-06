from typing import List


class Solution:
    # Using Prefix Sum
    # Time: O(N+Q), Space: O(N+Q)
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # Initialize the result list with False values, one for each query.
        ans = [False] * len(queries)

        # Initialize a prefix array to track the count of indices with the same parity as the previous index
        # (violative indices)
        prefix = [0] * len(nums)
        prefix[0] = 0  # The first element cannot violate parity rules as it has no previous element

        # Build the prefix array
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                # Current and previous numbers have the same parity
                # Increment the count of violative indices in the prefix array
                prefix[i] = prefix[i - 1] + 1
            else:
                # Current and previous numbers have opposite parity
                # Carry forward the previous count
                prefix[i] = prefix[i - 1]

        # Process each query to determine if the range [start, end] is "special"
        for i in range(len(queries)):
            query = queries[i]
            start = query[0]  # Start index of the query range
            end = query[1]  # End index of the query range

            # Check if there are no violative indices in the range [start, end]
            # If prefix[end] - prefix[start] == 0, all adjacent elements in the range have opposite parity
            ans[i] = prefix[end] - prefix[start] == 0

        return ans

    # Brute Force - Gives TLE (Passes 535/536 Test Cases)
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        res = []
        for s, e in queries:
            parity = True
            for i in range(s, e):
                if not nums[i] % 2 != nums[i + 1] % 2:
                    parity = False
                    break
            res.append(parity)
        return res

    # Using & operator - Gives TLE (Passes 535/536 Test Cases)
    def isArraySpecial1(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        adj = []
        for i in range(len(nums) - 1):
            adj.append(nums[i] % 2 != nums[i + 1] % 2)

        res = []
        for s, e in queries:
            parity = True
            for i in range(s, e):
                parity &= adj[i]
                if not parity:
                    break
            res.append(parity)
        return res

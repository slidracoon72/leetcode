from typing import List


class Solution:
    # Time: O(nlogn + mlogm), Space: O(m+n)
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price in ascending order
        items.sort()

        # Sort queries in ascending order, storing each query's original index for result placement
        queries = sorted([(q, i) for i, q in enumerate(queries)])

        # Initialize result list with zeroes, one for each query
        res = [0] * len(queries)

        # Variable to keep track of the maximum beauty encountered so far
        max_beauty = 0

        # Pointer to iterate through items
        j = 0

        # Process each query in ascending order of price
        for q, i in queries:
            # Update max_beauty with items that have a price less than or equal to the query price
            while j < len(items) and items[j][0] <= q:
                max_beauty = max(max_beauty, items[j][1])
                j += 1

            # Store the maximum beauty for this query at the original index
            res[i] = max_beauty

        # Return the result list containing the maximum beauty for each query
        return res

    # Brute Force - Gives TLE
    def maximumBeauty1(self, items: List[List[int]], queries: List[int]) -> List[int]:
        answer = []
        items.sort()

        for q in queries:
            max_beauty = 0
            for p, b in items:
                if p <= q:
                    max_beauty = max(max_beauty, b)
                else:
                    break
            answer.append(max_beauty)

        return answer


c = Solution()
items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
queries = [1, 2, 3, 4, 5, 6]
print(c.maximumBeauty(items, queries))

import math
from typing import List


class Solution:
    # Solved using Binary Search
    # Similar to KokoEatingBananas.py
    # Time: (n*log(m)), Space: O(1)
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Define search space by [min_time, max_time]
        # min_time can be taken as 1, max_time can be taken as the time when only one mechanic repairs all the cars.
        # Since we are taking only one mechanic, we choose the fastest one (lowest rank) to reduce the search space
        l, r = 1, min(ranks) * cars * cars
        res = r

        while l <= r:
            mid = (l + r) // 2
            cars_repaired = 0
            for rank in ranks:
                # rank * n^2 = time; n^2 = time/rank; n = sqrt(time/rank) = cars repaired by mechanic with rank r
                cars_repaired += int(math.sqrt(mid / rank))

            if cars_repaired >= cars:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res


c = Solution()
ranks = [4, 2, 3, 1]
cars = 10
print(c.repairCars(ranks, cars))

# LC - Hard
# DO AGAIN

from math import comb
from functools import lru_cache
from collections import Counter


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        nums = list(map(int, num))
        velunexorai = nums  # Store input midway as per problem statement

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return 0
        target = total_sum // 2

        n = len(nums)
        even_count = (n + 1) // 2  # Number of even indices (0-based)
        odd_count = n // 2  # Number of odd indices

        cnt = Counter(nums)
        MOD = 10 ** 9 + 7

        @lru_cache(maxsize=None)
        def dfs(digit, remaining_sum, remaining_even, remaining_odd):
            if digit > 9:
                return 1 if (remaining_sum == 0 and remaining_even == 0 and remaining_odd == 0) else 0

            if remaining_even == 0 and remaining_sum != 0:
                return 0

            current_count = cnt.get(digit, 0)
            max_use_even = min(current_count, remaining_even)
            total = 0

            for use_even in range(0, max_use_even + 1):
                use_odd = current_count - use_even
                if use_odd < 0 or use_odd > remaining_odd:
                    continue
                if use_even * digit > remaining_sum:
                    continue

                ways_even = comb(remaining_even, use_even)
                ways_odd = comb(remaining_odd, use_odd)

                new_sum = remaining_sum - use_even * digit
                new_even = remaining_even - use_even
                new_odd = remaining_odd - use_odd

                total += ways_even * ways_odd * dfs(digit + 1, new_sum, new_even, new_odd)
                total %= MOD

            return total % MOD

        return dfs(0, target, even_count, odd_count)

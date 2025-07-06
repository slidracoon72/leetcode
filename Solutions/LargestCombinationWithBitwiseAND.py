# 2275. Largest Combination With Bitwise AND Greater Than Zero
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Initialize an array to count the number of candidates that have each bit position set
        count = [0] * 32  # 32 bits for each position (enough for typical 32-bit integers)

        # Iterate over each candidate number
        for c in candidates:
            i = 0  # Start with the least significant bit (rightmost bit)
            while c > 0:
                # Check if the least significant bit is set (1) using bitwise AND
                count[i] += c & 1

                # Move to the next bit position
                i += 1

                # Right shift the candidate by 1 bit to process the next bit in the next iteration
                c = c >> 1

        # The largest combination is the maximum count of any bit position,
        # which shows how many numbers share a common set bit in that position.
        return max(count)

    def largestCombination1(self, candidates: List[int]) -> int:
        res = 0  # Initialize the result to store the maximum count of set bits in any position

        # Loop through each bit position from 0 to 31 (for 32-bit integers)
        for i in range(32):
            cnt = 0  # Counter to keep track of how many numbers have the ith bit set

            # Check each number in candidates to see if the ith bit is set
            for c in candidates:
                # Shift 1 to the ith position and perform a bitwise AND with the candidate
                # If the result is non-zero, it means the ith bit in the candidate is set
                cnt += 1 if (1 << i) & c else 0

            # Update the result with the maximum count found for any bit position
            res = max(res, cnt)

        # Return the maximum count of candidates with a common set bit in any position
        return res


sol = Solution()
candidates = [16, 17, 71, 62, 12, 24, 14]
print(sol.largestCombination(candidates))
print(sol.largestCombination1(candidates))

from typing import List


class Solution:
    # Solved using Prefix-Sum
    # Time: O(n^2) - Gives TLE
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum = [0]
        for i in range(len(arr)):
            prefix_sum.append(prefix_sum[-1] + arr[i])

        res = 0
        for i in range(1, len(prefix_sum)):
            for j in range(i, len(prefix_sum)):
                subarray_sum = prefix_sum[j] - prefix_sum[i - 1]
                if subarray_sum % 2:
                    res += 1

        return res

    # Time: O(n), Space: O(1)
    def numOfSubarrays1(self, arr: List[int]) -> int:
        prefix_sum = 0  # Running prefix sum of the array elements
        odd_cnt = 0  # Count of prefix sums that are odd (excluding current)
        even_cnt = 0  # Count of prefix sums that are even (excluding current)
        res = 0  # Result: total number of subarrays with odd sum
        MOD = 10 ** 9 + 7  # Modulo constant to handle large results as per problem constraint

        for num in arr:  # Iterate through each element in the array
            prefix_sum += num  # Update the running prefix sum with current number

            if prefix_sum % 2:  # If current prefix sum is odd
                # Add 1 (for subarray starting at index 0 ending here) + even_cnt (prior even sums)
                # Each prior even prefix sum paired with this odd sum gives an odd subarray
                res = (res + 1 + even_cnt) % MOD
                odd_cnt += 1  # Increment count of odd prefix sums
            else:  # If current prefix sum is even
                # Add odd_cnt (prior odd sums), as each pairs with this even sum to give odd subarray
                res = (res + odd_cnt) % MOD
                even_cnt += 1  # Increment count of even prefix sums

        return res  # Return total count of subarrays with odd sum


c = Solution()
print(c.numOfSubarrays([1, 3, 5]))  # Output: 4
print(c.numOfSubarrays([2, 4, 6]))  # Output: 0

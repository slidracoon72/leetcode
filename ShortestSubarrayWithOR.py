from typing import List


class Solution:
    # Using Sliding Window Approach
    # Neetcode: https://www.youtube.com/watch?v=Bq_BEsgBQOs&ab_channel=NeetCodeIO
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float("inf")
        bits = [0] * 32

        l = 0
        for r in range(len(nums)):
            # set bits of nums[r] in bits
            for i in range(32):
                if nums[r] & (1 << i):
                    bits[i] += 1

            # calculate OR of current subarray (i.e. bits set until now in bits array)
            cur_or = 0
            for i in range(32):
                if bits[i]:
                    cur_or += (1 << i)

            # shrink window
            while l <= r and cur_or >= k:
                # update res with min length of subarray
                res = min(res, r - l + 1)

                # reduce the bits of nums[l]
                for i in range(32):
                    if nums[l] & (1 << i):
                        bits[i] -= 1

                # update cur_or
                cur_or = 0
                for i in range(32):
                    if bits[i]:
                        cur_or += (1 << i)

                # update l, reduce window by incrementing left
                l += 1

        return res if res != float("inf") else -1

    # Time: O(n), Space: O(1)
    def minimumSubarrayLength1(self, nums: List[int], k: int) -> int:
        # Initialize a frequency array for each bit in a 32-bit integer
        bits_freq = [0] * 32

        # Function to calculate the OR of all elements represented by the bit frequencies
        def get_or(bits_freq):
            b_or = 0  # Variable to store the cumulative OR value
            for bit in range(32):  # Iterate over all 32 bits
                if bits_freq[bit] > 0:  # If the bit has been set in the frequency list
                    b_or |= (1 << bit)  # Set that bit in the OR result
            return b_or

        # Function to add a number's bits to the frequency array
        def add_to_bits_freq(bits_freq, n):
            for bit in range(32):  # Iterate over all 32 bits
                if (n >> bit) & 1:  # Check if the bit is set in number 'n'
                    bits_freq[bit] += 1  # Increment the frequency of that bit

        # Function to remove a number's bits from the frequency array
        def remove_from_bits_freq(bits_freq, n):
            for bit in range(32):  # Iterate over all 32 bits
                if (n >> bit) & 1:  # Check if the bit is set in number 'n'
                    bits_freq[bit] -= 1  # Decrement the frequency of that bit

        i = 0  # Left pointer of the sliding window
        res = float("inf")  # Initialize result to infinity (no valid subarray found yet)
        n = len(nums)  # Get the length of the input array

        for j in range(n):  # Iterate over the array with the right pointer (j)
            # Expand the window by adding the current element's bits to the frequency array
            add_to_bits_freq(bits_freq, nums[j])

            # Get the OR of the current window represented by the bit frequencies
            cur_or = get_or(bits_freq)

            # Shrink the window from the left while the OR value is greater than or equal to k
            while i <= j and cur_or >= k:
                # Update the result with the length of the current valid subarray
                res = min(res, j - i + 1)

                # Remove the leftmost element's bits from the frequency array
                remove_from_bits_freq(bits_freq, nums[i])

                # Recalculate the OR after removing the leftmost element
                cur_or = get_or(bits_freq)

                # Move the left pointer (i) to the right to shrink the window
                i += 1

        # If no valid subarray was found, return -1. Otherwise, return the smallest length.
        return res if res != float("inf") else -1


c = Solution()
nums = [2, 1, 8]
k = 10
print(c.minimumSubarrayLength(nums, k))

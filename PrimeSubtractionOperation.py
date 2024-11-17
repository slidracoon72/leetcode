from math import sqrt
from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=G9cp9y45qEs&ab_channel=NeetCodeIO
    # Time: O(n * m * sqrt(m))
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Helper function to check if a number is prime
        def is_prime(n):
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:  # If n has a factor other than 1 and itself, it is not prime
                    return False
            return True  # n is prime if it has no divisors up to its square root

        prev = 0  # Variable to keep track of the previous adjusted number in sequence
        for n in nums:
            # Define the upper limit for the prime number search to keep `n - largest_prime` > `prev`
            upper_bound = n - prev  # Exclusive upper bound to avoid going over `n`

            # Find the largest prime less than upper_bound
            largest_prime = 0
            for i in reversed(range(2, upper_bound)):  # Iterate backwards for efficiency
                if is_prime(i):  # Check if i is prime
                    largest_prime = i  # Set i as the largest prime found
                    break  # Stop as soon as we find the largest prime below upper_bound

            # Check if the current number minus the largest prime is valid and increasing
            if n - largest_prime <= prev:
                return False  # Return False if the sequence is not strictly increasing

            # Update prev to the current adjusted number for the next iteration
            prev = n - largest_prime

        return True  # If the loop completes, the sequence is strictly increasing


c = Solution()
nums = [4, 9, 6, 10]
print(c.primeSubOperation(nums))

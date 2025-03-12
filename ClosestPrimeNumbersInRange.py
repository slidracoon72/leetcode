from math import ceil, sqrt
from typing import List


class Solution:
    # Brute Force - Gives TLE (Passes 25/66 testcases)
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n) -> bool:
            for i in range(2, ceil(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        primes = []
        for i in range(left, right + 1):
            if isPrime(i):
                primes.append(i)

        if len(primes) < 2:
            return [-1, -1]

        res = [0, 0]
        diff = float('inf')
        for i in range(len(primes) - 1, 0, -1):
            big = primes[i]
            small = primes[i - 1]
            if big - small <= diff:
                res = [small, big]
                diff = big - small

        return res

    # Using Sieve of Eratosthenes
    def closestPrimes1(self, left: int, right: int) -> List[int]:
        # Early exit if range can't contain primes
        if right < 2 or left > right:
            return [-1, -1]

        def get_primes():
            # Initialize sieve array
            is_prime = [True] * (right + 1)  # mark all as prime (True)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are non-prime

            # Sieve to mark non-primes
            for n in range(2, int(sqrt(right)) + 1):
                if not is_prime[n]:
                    continue
                for m in range(n + n, right + 1, n):
                    is_prime[m] = False

            # Collect primes >= left efficiently
            primes = [i for i in range(max(2, left), right + 1) if is_prime[i]]
            return primes

        # Get primes in range
        primes = get_primes()

        # Default result if < 2 primes
        res = [-1, -1]
        if len(primes) < 2:
            return res

        # Find smallest gap between consecutive primes
        diff = right - left + 1
        for i in range(len(primes) - 1):
            current_diff = primes[i + 1] - primes[i]
            if current_diff < diff:
                diff = current_diff
                res = [primes[i], primes[i + 1]]
            # Early exit if smallest possible gap found
            if diff == 2:
                break

        return res


c = Solution()
print(c.closestPrimes1(10, 19))
print(c.closestPrimes1(4, 6))

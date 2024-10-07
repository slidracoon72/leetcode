from typing import List, Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Create a frequency counter for remainders when each element in arr is divided by k
        f = Counter(x % k for x in arr)

        # Iterate over the unique remainders (keys) in the frequency counter
        for key in f.keys():
            # Find the "other_key" that when added to "key" makes a sum divisible by k
            other_key = (k - key) % k

            # Special case: if the key is equal to other_key, it means the remainder is 0
            # or half of k (if k is even). In this case, we need an even count of such elements.
            if key == other_key:
                if f[key] % 2 != 0:
                    # If there is an odd count of elements with this remainder, return False
                    return False
            else:
                # For non-matching keys, ensure that the counts of elements with remainder 'key'
                # match the counts of elements with remainder 'other_key' to form valid pairs
                if f[key] != f[other_key]:
                    return False

        # If all conditions are met, return True
        return True

from collections import Counter
from typing import List


class FindSumPairs:
    # Solved using Hash-Map
    # Similar to TwoSum.py
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        new = old + val

        self.freq2[old] -= 1
        if self.freq2[old] == 0:
            del self.freq2[old]

        self.freq2[new] += 1
        self.nums2[index] = new

    def count(self, tot: int) -> int:
        count = 0
        for n1 in self.nums1:
            complement = tot - n1
            if complement in self.freq2:
                count += self.freq2[complement]

        return count

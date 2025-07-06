# 1460. Make Two Arrays Equal by Reversing Sub-Arrays
from collections import Counter, defaultdict
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)

    def canBeEqual1(self, target: List[int], arr: List[int]) -> bool:
        t = Counter(target)
        a = Counter(arr)
        return t == a
        # return Counter(target) == Counter(arr)

    def canBeEqual2(self, target: List[int], arr: List[int]) -> bool:
        t, a = defaultdict(int), defaultdict(int)

        for i in range(len(target)):
            t[target[i]] += 1
            a[arr[i]] += 1

        return t == a

    def canBeEqual3(self, target: List[int], arr: List[int]) -> bool:
        t, a = defaultdict(int), defaultdict(int)

        for n1, n2 in zip(target, arr):
            t[n1] += 1
            a[n2] += 1

        if len(t) != len(a):
            return False

        for n in t:
            if t[n] != a[n]:
                return False

        return True

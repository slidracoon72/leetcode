# LC - Hard
# DO AGAIN

from typing import List


class Solution:
    # Brute Force - Gives MLE
    # Passes 77/148 test cases
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        trip1, trip2 = set(), set()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    trip1.add((nums1[i], nums1[j], nums1[k]))
                    trip2.add((nums2[i], nums2[j], nums2[k]))

        # res = 0
        # for t in trip1:
        #     if t in trip2:
        #         res += 1
        # return res
        return len(trip1 & trip2)


c = Solution()
nums1 = [4, 0, 1, 3, 2]
nums2 = [4, 1, 0, 2, 3]
print(c.goodTriplets(nums1, nums2))


# LC - Editorial Solution
class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2, reversedIndexMapping = [0] * n, [0] * n
        for i, num2 in enumerate(nums2):
            pos2[num2] = i
        for i, num1 in enumerate(nums1):
            reversedIndexMapping[pos2[num1]] = i
        tree = FenwickTree(n)
        res = 0
        for value in range(n):
            pos = reversedIndexMapping[value]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n - 1 - pos) - (value - left)
            res += left * right
        return res

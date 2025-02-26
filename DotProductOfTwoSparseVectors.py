from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for x, y in zip(self.array, vec.array):
            res += x * y
        return res


# Using Hash Table
class SparseVector1:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # iterate through each non-zero element in this sparse vector
        # update the dot product if the corresponding index has a non-zero value in the other vector
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result


nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
res = v1.dotProduct(v2)
print(res)

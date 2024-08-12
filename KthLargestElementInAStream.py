import heapq
from typing import List


# My Solution
# Time: O(nlogn), Space: O(n)
# Solved Using Array
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.k]


# Neetcode: https://www.youtube.com/watch?v=hOjcdrqMoQ8
# More optimal solution using Min-Hap
class KthLargest1:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        # Convert array to min-heap
        heapq.heapify(self.minHeap)
        # Keep only k largest elements in min-heap
        # Suppose, k = 3, nums = [1,2,3,4,5,6]
        # We keep only [4,5,6]. Then 4 is the kth (here, 3rd) largest element of nums
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add value to heap
        heapq.heappush(self.minHeap, val)
        # Maintain only k-largest elements after push
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Return smallest element of K remaining elements
        return self.minHeap[0]


k = 3
nums = [4, 5, 8, 2]
obj = KthLargest1(k, nums)
values = [3, 5, 10, 9, 4]

for val in values:
    print(obj.add(val))

class Solution:
    def mySqrt(self, x: int) -> int:
        # Using binary search
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last


v = Solution()
print(v.mySqrt(64))
print(v.mySqrt(81))
print(v.mySqrt(110))

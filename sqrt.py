class Solution:
    # Using Binary Search -> Time: O(log n)
    def mySqrt(self, x: int) -> int:
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

    # Neetcode: https://www.youtube.com/watch?v=zdMhGxRWutQ
    # Using Binary Search -> Time Complexity: O(log n)
    def mySqrt1(self, x: int) -> int:
        # Initialize the left and right pointers for the binary search
        l, r = 0, x
        # Variable to store the potential integer square root
        res = 0

        # Perform binary search to find the integer square root
        while l <= r:
            # Calculate the midpoint to avoid overflow
            mid = l + (r - l) // 2
            # If mid squared is greater than x, search in the left half
            if mid ** 2 > x:
                r = mid - 1
            # If mid squared is less than x, search in the right half
            elif mid ** 2 < x:
                l = mid + 1
                # This value might be a possible result if no exact square root is found
                res = mid
            else:
                # If mid squared equals x, mid is the exact square root
                return mid
        # Return the integer part of the square root if no exact square root is found
        return res


v = Solution()
print(v.mySqrt(64))
print(v.mySqrt(81))
print(v.mySqrt(110))

print(v.mySqrt1(64))
print(v.mySqrt1(81))
print(v.mySqrt1(110))

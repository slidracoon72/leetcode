class Solution(object):
    def largestPerimeter(self, A):
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i + 1] > A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0


c = Solution()
nums = [1, 2, 1, 10]
print(c.largestPerimeter(nums))

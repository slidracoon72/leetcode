class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        # Get sum for starting window
        sum = 0
        for i in range(0, k):
            sum += nums[i]
        maxSum = sum

        # Start sliding window
        startIndex = 0
        endIndex = k

        while (endIndex < len(nums)):
            sum -= nums[startIndex]
            startIndex += 1

            sum += nums[endIndex]
            endIndex += 1

            maxSum = max(maxSum, sum)

        return maxSum / k

    def findMaxAverage1(self, nums, k: int) -> float:
        l = 0
        r = l + k
        avg = 0
        while r < len(nums) + 1:
            add = 0
            for i in range(l, r):
                add += nums[i]
            if add >= 0:
                avg = max(avg, add)
            else:
                avg = min(avg, add)
            l += 1
            r += 1

        return avg / k


c = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(c.findMaxAverage(nums, k))
print(c.findMaxAverage1(nums, k))

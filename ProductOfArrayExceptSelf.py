class Solution:
    # Time: O(N), Space: O(1)
    # Neetcode: https://www.youtube.com/watch?v=bNvIQI2wAjk
    def productExceptSelf(self, nums):
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

    # This exceeds time limit
    def my_solution(self, nums):
        answer = []
        for i in range(len(nums)):
            d = nums[i]
            nums.remove(d)
            # print(nums)
            result = 1
            for x in nums:
                result *= x
            answer.append(result)
            nums.insert(i, d)

        return answer


c = Solution()
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]
print(c.productExceptSelf(nums1))
print(c.productExceptSelf(nums2))
print(c.my_solution(nums1))
print(c.my_solution(nums2))

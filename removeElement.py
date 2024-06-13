nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

if len(nums) == 0:
    print(0)
for i in nums:
    if i == val:
        nums.remove(i)

print("Before:", nums)
if nums.pop() == val:
    nums.remove(nums[-1])

print("After:", nums)
print(len(nums))

print("------")


# Solution 2
class Solution:
    def remove_element(self, nums, val) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
                print(nums)
        print(nums)
        return i + 1


c = Solution()
print(c.remove_element(nums, val))

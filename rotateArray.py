nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

# nums = [-1, -100, 3, 99]
# k = 2

# Solution 1
nums1 = list()
c = 0
for i in range(len(nums) - 1, -1, -1):
    nums1.append(nums[i])
    c += 1
    if c == k:
        break

nums1.reverse()
nums2 = nums[:len(nums) - k]
# nums = nums1 + nums2

# print(nums1)
# print(nums2)
# print(nums)

# ------------------------
# Solution 2 - Solved "in-place"
n = len(nums)
k = k % n
print(nums)
nums[:n - k] = nums[:n - k][::-1]  # reverse front part
print(nums)
nums[n - k:] = nums[n - k:][::-1]  # reverse back part
print(nums)
nums[:] = nums[::-1]  # reverse whole list
print(nums)

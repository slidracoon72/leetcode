class Solution(object):
    def removeDuplicates(self, nums):
        # Initialize an integer k that updates the kth index of the array...
        # only when the current element does not match either of the two previous indexes. ...
        k = 0
        # Traverse all elements through loop...
        for i in nums:
            # If the index does not match elements, count that element and update it...
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k  # Return k after placing the final result in the first k slots of nums...

    # Solved using two-pointers
    # Neetcode: https://www.youtube.com/watch?v=ycAq8iqh0TI
    def removeDulicates1(self, nums):
        l, r = 0, 0  # Initialize two pointers, l for writing position, r for reading position

        while r < len(nums):  # Iterate through the list with the right pointer
            count = 1  # Initialize count of current element
            # Expanding r to check for consecutive duplicates
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1  # Move right pointer to the next duplicate
                count += 1  # Increment the count of the current element

            # Keep at most 2 elements of the current value
            for i in range(min(2, count)):  # We use min(2, count) to allow at most 2 duplicates
                nums[l] = nums[r]  # Write the current element to the left pointer position
                l += 1  # Move the left pointer to the next position

            r += 1  # Move right pointer to the next new element

        return l  # Return the length of the modified list

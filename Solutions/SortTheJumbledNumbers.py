from typing import List


class Solution:
    # Time complexity: O(nlogn) due to sorting, Space complexity: O(n) for the dictionary and list
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_int = {}  # Dictionary to store mapped values and original indices for each number
        for i, n in enumerate(nums):  # Enumerate to get both index and value
            s = ""
            for x in str(n):  # Convert each digit of the number using the mapping
                s += str(mapping[int(x)])
            mapped_int[n] = (int(s), i)  # Store the mapped value and the original index

        # Sort nums based on the mapped value, and if they are the same, by their original index
        sorted_nums = sorted(nums, key=lambda x: (mapped_int[x][0], mapped_int[x][1]))

        return sorted_nums  # Return the sorted list


c = Solution()
# mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
# nums = [991, 338, 38]
mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = [789, 456, 123]
print(c.sortJumbled(mapping, nums))

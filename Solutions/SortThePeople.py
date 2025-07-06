from typing import List


# Time: O(nlogn)
# Space: O(n)
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Create a dictionary to map heights to names
        height_to_name = {}

        # Iterate through heights and names simultaneously
        for h, n in zip(heights, names):
            # Assign each name to its corresponding height in the dictionary
            height_to_name[h] = n

        # Initialize an empty list to store the result
        res = []

        # Sort the heights in descending order and iterate through them
        for h in reversed(sorted(height_to_name)):
            # Append the name corresponding to the current height to the result list
            res.append(height_to_name[h])

        # Return the list of names sorted by height in descending order
        return res


c = Solution()
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
print(c.sortPeople(names, heights))

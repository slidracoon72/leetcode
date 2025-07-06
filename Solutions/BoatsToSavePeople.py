from typing import List


class Solution:
    # Two-Pointers
    # Time: O(nlogn), Space: O(1)
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the people by weight in ascending order
        people.sort()

        n = len(people)
        l, r = 0, n - 1  # Two pointers: l starts from the lightest, r from the heaviest
        res = 0  # Result variable to count the number of boats

        # Loop until all people are considered
        while l <= r:
            temp = people[l] + people[r]  # Check if the lightest and heaviest can share a boat

            if temp <= limit:
                # If together they are within limit, pair them
                res += 1
                l += 1  # Move left pointer (lightest person)
                r -= 1  # Move right pointer (heaviest person)
            else:
                # If too heavy together, the heavier person goes alone
                res += 1
                r -= 1  # Move right pointer only

        return res  # Return the total number of boats needed


c = Solution()
people = [3, 2, 2, 1]
limit = 3
print(c.numRescueBoats(people, limit))

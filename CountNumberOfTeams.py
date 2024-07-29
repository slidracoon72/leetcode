from typing import List


class Solution:
    # Not efficient - TLE
    # Time: O(n^3)
    def numTeams(self, rating: List[int]) -> int:
        length = len(rating)
        teams = 0

        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    # Count increasing teams
                    if rating[i] < rating[j] < rating[k]:
                        teams += 1
                    # Count decreasing teams
                    if rating[i] > rating[j] > rating[k]:
                        teams += 1

        return teams

    # Greedy Algorithm
    # Time: O(n^2), Space: O(1)
    # Neetcode: https://www.youtube.com/watch?v=zONHzIqCr-o
    def numTeams1(self, rating: List[int]) -> int:
        length = len(rating)
        teams = 0

        # Iterate over each element as the middle value of the team
        for m in range(1, length - 1):
            # finding increasing values (forward pass)
            # Initialize counters for values smaller and larger than the middle value
            left_smaller = right_larger = 0

            # Count how many values to the left of m are smaller than rating[m]
            for i in range(m):
                if rating[i] < rating[m]:
                    left_smaller += 1
            # Count how many values to the right of m are larger than rating[m]
            for i in range(m + 1, length):
                if rating[i] > rating[m]:
                    right_larger += 1

            teams += left_smaller * right_larger

            # finding decreasing values (backward pass)

            # m = no. of values to left of m
            left_larger = m - left_smaller
            # (length - m - 1) = no. of values to right of m
            right_smaller = (length - m - 1) - right_larger

            teams += left_larger * right_smaller

        return teams


c = Solution()
# rating = [2, 5, 3, 4, 1]
# rating = [2, 1, 3]
rating = [1, 2, 3, 4]
print(c.numTeams(rating))
print(c.numTeams1(rating))

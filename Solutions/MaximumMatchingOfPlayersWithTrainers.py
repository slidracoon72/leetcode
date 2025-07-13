from typing import List


class Solution:
    # Using Two-Pointers approach
    # Time: O(nlogn), Space: O(1)
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Sort both lists in ascending order
        # This allows us to match the weakest player with the weakest trainer that can support them
        players.sort()
        trainers.sort()

        res = 0  # Counter for number of matched player-trainer pairs
        i, j = 0, 0  # Pointers for players and trainers respectively

        # Iterate through both lists
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                # If the current trainer can handle the current player, match them
                res += 1
                i += 1  # Move to next player
                j += 1  # Move to next trainer
            else:
                # If trainer is too weak, try the next stronger trainer
                j += 1

        return res  # Return total number of successful matches


c = Solution()
players = [4, 7, 9]
trainers = [8, 2, 5, 8]
print(c.matchPlayersAndTrainers(players, trainers))
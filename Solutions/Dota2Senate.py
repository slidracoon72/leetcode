from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()  # Queues to track indices of Dire and Radiant senators
        n = len(senate)

        # Initialize the queues with indices of each party member
        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)  # Add Radiant senator's index to R queue
            else:
                D.append(i)  # Add Dire senator's index to D queue

        # Simulate rounds until one party is eliminated
        while D and R:
            dTurn = D.popleft()  # Get the next Dire senator's index
            rTurn = R.popleft()  # Get the next Radiant senator's index

            # The senator with the lower index bans the other
            # The winning senator gets re-added to the queue with updated index (+n)
            if rTurn < dTurn:
                R.append(rTurn + n)  # Radiant senator bans Dire and returns in next round
            else:
                D.append(dTurn + n)  # Dire senator bans Radiant and returns in next round

        # The party with senators remaining in their queue wins
        return "Radiant" if R else "Dire"


c = Solution()
senate = "RDDRDD"
print(c.predictPartyVictory(senate))

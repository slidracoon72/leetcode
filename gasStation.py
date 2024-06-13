class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        # Solving using Greedy Algorithm (Time: O(n), Space: O(1))
        if sum(cost) > sum(gas):
            return -1

        fuel = 0
        index = 0

        for i in range(len(gas)):
            fuel += gas[i] - cost[i]  # Difference of fuel left after journey

            if fuel < 0:
                fuel = 0
                index = i + 1

        return index


c = Solution()

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

gas1 = [2, 3, 4]
cost1 = [3, 4, 3]

print(c.canCompleteCircuit(gas, cost))
print(c.canCompleteCircuit(gas1, cost1))

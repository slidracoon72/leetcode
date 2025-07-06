from collections import defaultdict, deque
from typing import List


class Solution:
    # Time: O(N), Space: O(N)
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Build adjacency list representation of the tree
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Track Bob's arrival time at each node on his path to 0 using DFS
        bob_time = {}  # node -> time

        def bob_path(node, parent, time):
            bob_time[node] = time
            if node == 0:  # Reached root
                return True
            for neighbor in graph[node]:
                if neighbor != parent and bob_path(neighbor, node, time + 1):
                    return True
            del bob_time[node]  # Remove if not on path to 0
            return False

        # Run Bob's path from his starting node
        bob_path(bob, -1, 0)

        # DFS for Alice to find max income
        def alice_dfs(node, parent, time, income):
            # Calculate income at current node based on Bob's timing
            curr_amount = amount[node]
            if node in bob_time:
                if bob_time[node] == time:  # Simultaneous arrival, split cost/reward
                    curr_amount //= 2
                elif bob_time[node] < time:  # Bob passed earlier, gate is open
                    curr_amount = 0

            income += curr_amount

            # Identify children (exclude parent)
            children = [n for n in graph[node] if n != parent]
            if not children:  # Leaf node
                return income

            # Explore all paths to leaves and take maximum
            max_income = float('-inf')
            for child in children:
                max_income = max(max_income, alice_dfs(child, node, time + 1, income))
            return max_income

        # Start Alice at node 0
        return alice_dfs(0, -1, 0, 0)


c = Solution()
edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
bob = 3
amount = [-2, 4, 2, -4, 6]
print(c.mostProfitablePath(edges, bob, amount))


# Similar approach as above, but using BFS for Alice and DFS for Bob
# Neetcode: https://www.youtube.com/watch?v=mESeQZKfvtY
class Solution1:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Build adjacency list for the undirected tree
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)  # Add edge from n1 to n2
            adj[n2].append(n1)  # Add edge from n2 to n1 (undirected)

        # Bob simulation - DFS to find his path to root (node 0)
        bob_times = {}  # Dictionary to store nodes Bob visits and his arrival time

        def bob_dfs(node, parent, time):
            # Base case: Bob reaches the root
            if node == 0:
                bob_times[node] = time  # Record time Bob arrives at node 0
                return True  # Indicate path to root found

            # Explore neighbors
            for nei in adj[node]:
                if nei != parent and bob_dfs(nei, node, time + 1):  # Avoid parent, recurse deeper
                    bob_times[node] = time  # Record time only if this node is on path to root
                    return True  # Propagate success up the call stack
            return False  # No path to root through this node

        # Start Bob's DFS from his initial node with no parent and time 0
        bob_dfs(bob, -1, 0)

        # Alice simulation - BFS to explore all paths to leaf nodes
        q = deque([(0, -1, 0, amount[0])])  # Queue: (node, parent, time, total_profit), start at node 0
        res = float('-inf')  # Track maximum profit Alice can achieve
        while q:
            node, parent, time, profit = q.popleft()  # Dequeue current state

            # Process each neighbor of the current node
            for nei in adj[node]:
                if nei == parent:  # Skip the parent to avoid backtracking
                    continue
                nei_time = time + 1  # Time to reach neighbor (one step from current node)
                nei_profit = amount[nei]  # Base profit/cost at neighbor node

                # Adjust profit based on Bob's timing
                if nei in bob_times:
                    if nei_time == bob_times[nei]:  # Alice and Bob arrive simultaneously
                        nei_profit = nei_profit // 2  # Split the cost/reward evenly
                    elif nei_time > bob_times[nei]:  # Alice arrives after Bob
                        nei_profit = 0  # Gate already open, no cost or reward

                # Calculate total profit for this path
                total_profit = profit + nei_profit
                # Add neighbor to queue for further exploration
                q.append((nei, node, nei_time, total_profit))

                # Check if neighbor is a leaf node (only connected to current node)
                if len(adj[nei]) == 1:
                    res = max(res, total_profit)  # Update max profit if leaf reached

        return res  # Return the maximum profit Alice can achieve


c = Solution1()
edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
bob = 3
amount = [-2, 4, 2, -4, 6]
print(c.mostProfitablePath(edges, bob, amount))

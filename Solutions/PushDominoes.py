import collections


class Solution:
    # Solved using BFS - Simultaneous falling of dominoes each second
    # Neetcode: https://www.youtube.com/watch?v=evUFsOb_iLY&ab_channel=NeetCode
    # Time: O(n), Space: O(n)
    def pushDominoes(self, dominoes: str) -> str:
        # Convert the input string to a list for easier modification
        dom = list(dominoes)
        # Use deque to simulate BFS-like processing of domino pushes
        q = collections.deque()

        # Initialize the queue with all dominoes that are not upright ('.')
        for i, d in enumerate(dom):
            if d != ".":
                q.append((i, d))

        # Process the queue until all falling forces are applied
        while q:
            i, d = q.popleft()

            if d == "L":
                # If current domino falls to the left and the left neighbor is upright
                if i > 0 and dom[i - 1] == ".":
                    # Push the left neighbor to fall left
                    q.append((i - 1, "L"))
                    dom[i - 1] = "L"

            elif d == "R":
                # If current domino falls to the right and the right neighbor is upright
                if i + 1 < len(dom) and dom[i + 1] == ".":
                    # Check if a left-falling domino is already scheduled two steps ahead
                    # If so, the forces cancel each other, so skip adding the right push
                    if i + 2 < len(dom) and dom[i + 2] == "L":
                        q.popleft()  # cancel out opposing force
                    else:
                        # Push the right neighbor to fall right
                        q.append((i + 1, "R"))
                        dom[i + 1] = "R"

        # Convert the list back to string and return the final state
        return "".join(dom)


c = Solution()
dominoes = ".L.R...LR..L.."
print(c.pushDominoes(dominoes))

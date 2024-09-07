from typing import List


# Neetcode: https://www.youtube.com/watch?v=wpglWC6mnLg
# Time: O(n+k), Space:O(k) where n=len(commands), k=len(obstacles)
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Initial position
        x, y = 0, 0

        # Arranged in clockwise position for easy way to keep track of directions
        # N, E, S, W
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0  # current directions index
        res = 0  # to store max distance

        # convert obstacles from list to set for faster O(1) lookup
        obstacles = {tuple(o) for o in obstacles}  # set comprehension

        for c in commands:
            # turn right
            if c == -1:
                # modding by 4 (=len(directions)) to stay in-bounds
                # Eg. N -> E, so we move d right (+1)
                d = (d + 1) % 4
            # turn left
            elif c == -2:
                # Eg. S -> E, so we move d left (-1)
                d = (d - 1) % 4
            # start walking
            else:
                dx, dy = directions[d]
                # walk one step at a time
                for _ in range(c):
                    # check if obstacle in path
                    if (x + dx, y + dy) in obstacles:
                        break
                    x, y = x + dx, y + dy
                res = max(res, x ** 2 + y ** 2)

        return res


c = Solution()
commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
print(c.robotSim(commands, obstacles))

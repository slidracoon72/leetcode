from typing import List
from collections import defaultdict


class Solution:
    # Time: O(N), Space: O(1)
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Initialize dictionaries to count frequencies of numbers in tops and bottoms
        t = defaultdict(int)
        b = defaultdict(int)

        # Count occurrences of each number in tops and bottoms arrays
        for top, bottom in zip(tops, bottoms):
            t[top] += 1
            b[bottom] += 1

        # Find the number with the highest frequency in tops and bottoms
        max_top = max(t.items(), key=lambda x: x[1])
        max_bottom = max(b.items(), key=lambda x: x[1])

        # Initialize variables to track the target number and whether it’s from tops
        max_occur = 0
        top = False
        # Choose the number with higher frequency (tops or bottoms); default to bottoms if equal
        if max_top[1] > max_bottom[1]:
            max_occur = max_top[0]
            top = True
        else:
            max_occur = max_bottom[0]

        # Initialize counter for minimum rotations needed
        res = 0
        # If targeting tops array, try to make all tops equal to max_occur
        if top:
            for ind, (i, j) in enumerate(zip(tops, bottoms)):
                # If top element differs from target, check if bottom matches
                if i != max_occur:
                    if j == max_occur:
                        # Rotate by setting top to bottom’s value (swap)
                        tops[ind] = j
                        res += 1
        # If targeting bottoms array, try to make all bottoms equal to max_occur
        else:
            for ind, (i, j) in enumerate(zip(bottoms, tops)):
                # If bottom element differs from target, check if top matches
                if i != max_occur:
                    if j == max_occur:
                        # Rotate by setting bottom to top’s value (swap)
                        bottoms[ind] = j
                        res += 1

        # Check if the target array (tops or bottoms) is uniform after rotations
        if top:
            # If tops is all same number, return rotations needed
            if len(set(tops)) == 1:
                return res
        else:
            # If bottoms is all same number, return rotations needed
            if len(set(bottoms)) == 1:
                return res

        # Return -1 if no valid solution is found (cannot make one row uniform)
        return -1


c = Solution()
tops = [2, 1, 2, 4, 2, 2]
bottoms = [5, 2, 6, 2, 3, 2]
print(c.minDominoRotations(tops, bottoms))

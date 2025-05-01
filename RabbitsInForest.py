from collections import defaultdict
from typing import List


class Solution:
    # Time: O(n), Space: O(n)
    def numRabbits(self, answers: List[int]) -> int:
        group_freq = defaultdict(int)  # Tracks how many rabbits have given each specific answer
        count = 0  # Final count of minimum rabbits in the forest

        for ele in answers:
            if ele == 0:
                # If a rabbit says 0, it means no other rabbits are like it, so it's alone
                count += 1
            else:
                group_freq[ele] += 1  # Count how many times this answer appears
                if group_freq[ele] == ele + 1:
                    # Once we have a complete group of (ele + 1) rabbits,
                    # we add them to the total and reset the group count
                    count += ele + 1
                    group_freq[ele] = 0  # Reset for possible next group of same size

        # For any incomplete group left (not reaching ele + 1), we still need to count a full group
        for group, freq in group_freq.items():
            if freq > 0:
                count += group + 1

        return count


c = Solution()
answers1 = [1, 1, 2]
answers2 = [10, 10, 10]
print(c.numRabbits(answers1))
print(c.numRabbits(answers2))

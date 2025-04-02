from collections import Counter
from typing import List


class Solution:
    # Time: O(n), Space: O(26) = O(1)
    def partitionLabels(self, s: str) -> List[int]:
        # Count frequency of each character in the string
        count = Counter(s)
        # Track characters currently in the partition
        visit = set()
        # Store the lengths of each partition
        res = []
        # Start index of the current partition
        j = 0

        # Iterate through each character in the string with its index
        for i, c in enumerate(s):
            # Add character to visit set if not already present
            if c not in visit:
                visit.add(c)
            # Decrement the count of the current character
            count[c] -= 1
            # If no more occurrences of this character remain
            if count[c] <= 0:
                # Remove from counter and visit set
                del count[c]
                visit.remove(c)
            # If visit set is empty, we've completed a partition
            if not visit:
                # Calculate partition length (i - j + 1) and add to result
                res.append(i - j + 1)
                # Update start index of next partition
                j = i + 1

        # Return the list of partition lengths
        return res

    # Time: O(n), Space: O(26) = O(1)
    def partitionLabels1(self, s: str) -> List[int]:
        last_index = {}

        for i, c in enumerate(s):
            last_index[c] = i

        res = []
        size, max_end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = last_index[c]
            max_end = max(max_end, end)

            if i == max_end:
                res.append(size)
                size = 0

        return res


c = Solution()
s = "ababcbacadefegdehijhklij"
print(c.partitionLabels(s))
print(c.partitionLabels1(s))

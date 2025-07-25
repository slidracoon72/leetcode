from typing import List, Counter


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rc = Counter(ranks)
        rc = rc.values()

        if len(set(suits)) == 1:
            return "Flush"

        for v in rc:
            if v >= 3:
                return "Three of a Kind"

        for v in rc:
            if v == 2:
                return "Pair"

        return "High Card"

    def bestHand1(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        rc = Counter(ranks)
        rc = set(rc.values())

        if 3 in rc or 4 in rc:
            return "Three of a Kind"
        if 2 in rc:
            return "Pair"

        return "High Card"


c = Solution()
ranks = [4, 4, 2, 4, 4]
suits = ["d", "a", "a", "b", "c"]
print(c.bestHand(ranks, suits))

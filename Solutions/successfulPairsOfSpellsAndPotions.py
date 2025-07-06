from typing import List


class MySolution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()
        for i in range(len(spells)):
            sp = 0
            m = len(potions)
            for j in range(len(potions)):
                product = spells[i] * potions[j]
                if product >= success:
                    sp += m
                    break
                else:
                    m -= 1
            pairs.append(sp)
        return pairs

# Using Binary Search
class OptimalSolution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()
        for spell in spells:
            count = self.binary_search(potions, spell, success)
            pairs.append(count)
        return pairs

    def binary_search(self, potions: List[int], spell_strength: int, success: int) -> int:
        left, right = 0, len(potions)
        while left < right:
            mid = (left + right) // 2
            if spell_strength * potions[mid] >= success:
                right = mid
            else:
                left = mid + 1
        return len(potions) - left

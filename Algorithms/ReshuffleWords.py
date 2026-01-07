from collections import defaultdict
from typing import List

old_positions = [3, 2, 4, 1, 0]
new_positions = [2, 4, 3, 0, 1]
words = ['cupcake', 'donut', 'eclair', 'froyo', 'gingerbread']
result = ['donut', 'eclair', 'cupcake', 'gingerbread', 'froyo']


class Solution:
    def shuffle(self, old_positions: List[int], new_positions: List[int], words: List[str]) -> List[str]:
        new_index = defaultdict(int)
        for i in range(len(words)):
            cur = new_positions[i]
            new_index[cur] = i

        res = [""] * len(words)
        for i in range(len(words)):
            cur = words[i]
            new = new_index[old_positions[i]]
            res[new] = cur

        return res


c = Solution()
print(c.shuffle(old_positions, new_positions, words))

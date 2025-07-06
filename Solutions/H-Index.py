from typing import List


# citations = [3, 0, 6, 1, 5]
# citations = [6, 5, 3, 1, 0] - sorted
# index =     [0, 1, 2, 3, 4]


class Solution:
    def hIndex(self, c: List[int]) -> int:
        c.sort(reverse=True)
        if len(c) == 1 and c[0] > 0:
            return 1
        if c[-1] >= len(c):
            return len(c)
        for i in range(len(c)):
            if c[i] < i + 1:
                return i
        return 0

# p = len(citations)
# index = 0
# for i in range(p):
#     if citations[i] <= p:
#         count = 0
#         for j in range(p):
#             if citations[j] >= citations[i]:
#                 count += 1
#         index = max(index, count)
#
# print(index)

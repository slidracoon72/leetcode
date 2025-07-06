from typing import List


# Time: O(n), Space: O(1)
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log == './':
                continue
            elif log == '../':
                count = max(0, count - 1)
            else:
                count += 1

        return count


c = Solution()
logs = ["d1/", "d2/", "../", "d21/", "./"]
print(c.minOperations(logs))

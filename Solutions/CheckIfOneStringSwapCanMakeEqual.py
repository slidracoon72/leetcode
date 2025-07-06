# LC - 1790: Check if One String Swap Can Make Strings Equal

class Solution:
    # Time: O(n), Space: O(1)
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Collect pairs where characters differ
        diff = []
        for a, b in zip(s1, s2):
            if a != b:
                diff.append((a, b))
            if len(diff) > 2:
                return False

        # If both strings are equal
        if len(diff) == 0:
            return True

        # Strings must have exactly two differences that can be swapped
        return len(diff) == 2 and diff[0] == diff[1][::-1]


c = Solution()
s1 = "bank"
s2 = "kanb"
print(c.areAlmostEqual(s1, s2))

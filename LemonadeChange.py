from typing import List


# Greedy Solution
# Time: O(n), Space: O(1)
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0, 20: 0}
        for b in bills:
            # collect money
            d[b] += 1

            # return change
            if b > 5:
                if b == 10:
                    if d[5] >= 1:
                        d[5] -= 1
                    else:
                        return False
                elif b == 20:
                    if d[5] >= 3:
                        d[5] -= 3
                    elif d[5] >= 1 and d[10] >= 1:
                        d[5] -= 1
                        d[10] -= 1
                    else:
                        return False
        return True

    # Neetcode Solution (Similar as mine)
    def lemonadeChange1(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        for b in bills:
            if b == 5:
                fives += 1
            if b == 10:
                tens += 1

            change = b - 5

            # if $10 received
            if change == 5:
                if fives > 0:
                    fives -= 1
                else:
                    return False
            # if $20 received
            elif change == 15:
                # return 10 and 5
                if fives > 0 and tens > 0:
                    fives, tens = fives - 1, tens - 1
                # return 3 5's
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True


c = Solution()
# bills = [5, 5, 5, 10, 20]
bills = [5, 5, 10, 10, 20]
print(c.lemonadeChange(bills))
print(c.lemonadeChange1(bills))

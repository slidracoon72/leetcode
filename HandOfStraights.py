from collections import Counter


class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True


c = Solution()
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(c.isNStraightHand(hand, groupSize))
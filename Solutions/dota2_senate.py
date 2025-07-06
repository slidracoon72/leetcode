class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire = []
        for ind, char in enumerate(senate):
            if char == 'R':
                radiant.append(ind)
            else:
                dire.append(ind)
        n = len(senate)
        lenr = len(radiant)
        lend = len(dire)
        while True:
            if lenr != 0 and lend == 0:
                return "Radiant"
            elif lend != 0 and lenr == 0:
                return "Dire"
            if radiant[0] < dire[0]:
                radiant.pop(0)
                dire.pop(0)
                radiant.append(n)
                lend -= 1
                n += 1
            else:
                radiant.pop(0)
                dire.pop(0)
                dire.append(n)
                lenr -= 1
                n += 1


c = Solution()
senate = "RDD"
print(c.predictPartyVictory(senate))

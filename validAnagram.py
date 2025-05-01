class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        return s == t

    # Time: O(nlogn + mlogm)
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    # Using Hash-Table
    # Time: O(n + m)
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True


s = "anagram"
t = "nagaram"
d1 = dict()
d2 = dict()
for i in s:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] += 1
for j in t:
    if j not in d2:
        d2[j] = 1
    else:
        d2[j] += 1
print(d1)
print(d2)
if d1 == d2:
    print("True")
else:
    print("False")

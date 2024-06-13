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

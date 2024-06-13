candies = [12, 1, 12]
extraCandies = 10
m = max(candies)
res = []
for x in candies:
    if x + extraCandies >= m:
        res.append(True)
    else:
        res.append(False)
print(res)

from bisect import bisect


def solution(operations):
    obstacles = set()
    res = []

    for op in operations:
        if op[0] == 1:
            obstacles.add(op[1])
        elif op[0] == 2:
            x, size = op[1], op[2]
            flag = True

            for i in range(x - size, x):
                if i in obstacles:
                    flag = False
                    break

            res.append("1" if flag else "0")

    return ''.join(res)


# More optimized
# Using Binary search
def solution(operations):
    obstacles = []
    res = []

    for op in operations:
        if op[0] == 1:
            bisect.insort(obstacles, op[1])
        elif op[0] == 2:
            x, size = op[1], op[2]
            start = x - size
            end = x - 1

            start_idx = bisect.bisect_left(obstacles, start)
            end_idx = bisect.bisect_right(obstacles, end)

            if start_idx != end_idx:
                res.append("0")
            else:
                res.append("1")

    return ''.join(res)

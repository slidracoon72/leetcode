# CISCO SWE-2 OA

# Question - 1: Design a chess board of (n * n) size
def funcChessBoard(inputNum):
    res = []
    for i in range(inputNum):
        row = []
        for j in range(inputNum):
            # Determine the color of the square
            if (i + j) % 2 == 0:
                row.append("W")
            else:
                row.append("B")
        res.append("".join(row))
    return res


def main():
    inputNum = int(input("Enter the size of the chessboard: "))
    if 0 < inputNum < 1000:
        result = funcChessBoard(inputNum)
        # Print each row of the result
        for row in result:
            print(row)
    else:
        print("Invalid input. N should be between 1 and 999.")


# main()


################################################################

# Question - 2: Find the smallest value of the person who is not a twin
def find_non_twin(inputArr):
    c = {}
    for n in inputArr:
        if n in c:
            c[n] += 1
        else:
            c[n] = 1

    res = float('inf')
    for k in c:
        if c[k] % 2 == 1:  # Check if the person is not a twin
            res = min(res, k)

    # If no non-twin is found, return -1
    return res if res != float('inf') else -1


def main1():
    # Input
    inputArr_size = int(input("Enter the size of the input array: "))
    inputArr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

    # Ensure input size matches array size
    if len(inputArr) != inputArr_size:
        print("Error: Input array size does not match the specified size.")
    else:
        result = find_non_twin(inputArr)
        print(result)


# main1()

################################################################

# Question - 3: Hop-Skip-Jump in anti-clockwise direction
def funcHopSkipJump(matrix):
    rows, cols = len(matrix), len(matrix[0])

    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    direction = 1
    hops = 0  # Counter to determine skip or hop
    last_hop = None  # Store the last cell Lucy hops onto

    while top <= bottom and left <= right:
        if direction == 0:  # Traverse left-to-right
            for i in range(left, right + 1):
                if hops % 2 == 0:  # If it's a hop
                    last_hop = matrix[top][i]
                hops += 1
            top += 1  # Move top boundary inward

        elif direction == 1:  # Traverse top-to-bottom
            for i in range(top, bottom + 1):
                if hops % 2 == 0:  # If it's a hop
                    last_hop = matrix[i][right]
                hops += 1
            right -= 1  # Move right boundary inward

        elif direction == 2:  # Traverse right-to-left
            for i in range(right, left - 1, -1):
                if hops % 2 == 0:  # If it's a hop
                    last_hop = matrix[bottom][i]
                hops += 1
            bottom -= 1  # Move bottom boundary inward

        elif direction == 3:  # Traverse bottom-to-top
            for i in range(bottom, top - 1, -1):
                if hops % 2 == 0:  # If it's a hop
                    last_hop = matrix[i][left]
                hops += 1
            left += 1  # Move left boundary inward

        # Change direction in anti-clockwise order (left-to-right -> top-to-bottom -> right-to-left -> bottom-to-top)
        direction = (direction + 1) % 4  # 0 -> 1 -> 2 -> 3 -> 0 -> ...

    return last_hop  # Return the last cell Lucy hopped onto


def main2():
    # Input
    rows, cols = map(int, input("Enter the number of rows and columns: ").split())
    matrix = []
    print("Enter the matrix row by row:")
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))

    # Output the last cell Lucy hops onto
    print(funcHopSkipJump(matrix))


main2()
################################################################

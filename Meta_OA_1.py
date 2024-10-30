# Q1 (all test cases passed)
def remove_vowels_and_reverse(inputString: str) -> str:
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    newStr = ""
    for s in inputString:
        if s not in vowels:
            newStr += s
    return newStr[::-1]


inputString = "The quick brown FOX jumps over the lazy DOG `1234."
print(remove_vowels_and_reverse(inputString))

###########################

# Q2 (all test cases passed)

from typing import List


def distribute_numbers(numbers: List[int]) -> List[int]:
    first, second = [numbers[0]], [numbers[1]]

    def count_greater(arr, value):
        count = 0
        for x in arr:
            if x > value:
                count += 1
        return count

    for i in range(2, len(numbers)):
        value = numbers[i]
        first_count = count_greater(first, value)
        second_count = count_greater(second, value)

        if first_count > second_count:
            first.append(value)
        elif second_count > first_count:
            second.append(value)
        elif len(first) < len(second):
            first.append(value)
        elif len(second) < len(first):
            second.append(value)
        else:
            first.append(value)

    return first + second


numbers = [5, 7, 6, 9, 2]
print(distribute_numbers(numbers))


###########################

# Q4 (all test cases passed)


def solution(a, b, queries):
    results = []
    b_count = {}

    # Initialize b_count with occurrences of each value in b
    for num in b:
        b_count[num] = b_count.get(num, 0) + 1

    for query in queries:
        if query[0] == 0:
            _, index, x = query
            # Update b_count for the old value
            b_count[b[index]] -= 1
            if b_count[b[index]] == 0:
                del b_count[b[index]]

            # Update the value in b and b_count for the new value
            b[index] += x
            b_count[b[index]] = b_count.get(b[index], 0) + 1

        elif query[0] == 1:
            _, x = query
            count = 0
            # Use .get to avoid KeyError
            for num in a:
                count += b_count.get(x - num, 0)
            results.append(count)

    return results


# a = [1, 2, 3]
a = [1, 2, 2]
# b = [1, 4]
b = [2, 3]
# queries = [[1, 5], [0, 0, 2], [1, 5]]
queries = [[1, 4], [0, 0, 1], [1, 5]]
print(solution(a, b, queries))


########################

# Q3 (Rhombus Question - Not passed)
def solution(matrix, radius):
    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')  # Initialize the maximum sum as the smallest possible number

    for centerX in range(rows):
        for centerY in range(cols):
            current_sum = 0  # Sum for the current rhombic area

            for dx in range(-radius, radius + 1):
                for dy in range(-radius + abs(dx), radius - abs(dx) + 1):
                    cellX, cellY = centerX + dx, centerY + dy

                    # Ensure the cell is within bounds
                    if 0 <= cellX < rows and 0 <= cellY < cols:
                        current_sum += matrix[cellX][cellY]

            # Update max_sum if we found a larger sum
            max_sum = max(max_sum, current_sum)

    return max_sum

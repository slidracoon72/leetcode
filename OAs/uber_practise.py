def is_valid_string(s: str) -> bool:
    """
    Check if the given string is valid.

    A valid string:
    1. Must be divisible by 3 when interpreted as a number.
    2. Must contain the digit '7' at least twice.

    Args:
    s (str): The input string.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    # Check if the string is divisible by 3
    if int(s) % 3 != 0:
        return False

    # Check if the string contains at least two '7's
    if s.count('7') < 2:
        return False

    return True


test_cases = ["771", "777", "123777", "12345", "71", "171", "70"]
for test in test_cases:
    print(f"String: {test}, Is valid: {is_valid_string(test)}")


#########################################################################

def command_frequency_counter(commands):
    """
    Counts the frequency of cmd1, cmd2, and cmd3 in the given command list.

    Args:
    commands (list): A list of commands containing cmd1, cmd2, cmd3, and references in the form of !<index>.

    Returns:
    list: A list of frequencies of cmd1, cmd2, and cmd3 in the order [freq of cmd1, freq of cmd2, freq of cmd3].
    """
    # Initialize counters for cmd1, cmd2, cmd3
    counts = [0, 0, 0]

    for i in range(len(commands)):
        # Check if the command is a reference like !<index>
        if commands[i][0] == '!':
            # Convert 1-based index in !<index> to 0-based index
            ref_index = int(commands[i][1:]) - 1
            # Replace the reference with the actual command
            commands[i] = commands[ref_index]

        # Increment the respective counter based on the command
        if commands[i] == "cmd1":
            counts[0] += 1
        elif commands[i] == "cmd2":
            counts[1] += 1
        elif commands[i] == "cmd3":
            counts[2] += 1

    return counts


# Test case
commands = ["cmd1", "cmd2", "cmd3", "!1", "!2", "cmd3", "cmd1"]
print(command_frequency_counter(commands))


#########################################################################

def find_regional_maxima(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    result = []

    def is_regional_maximum(i, j):
        cell = matrix[i][j]
        if cell == 0:
            return False

        # Define region boundaries
        top = max(0, i - cell)
        bottom = min(rows - 1, i + cell)
        left = max(0, j - cell)
        right = min(cols - 1, j + cell)

        # Check all valid cells in the region
        for x in range(top, bottom + 1):
            for y in range(left, right + 1):
                # Skip the corners
                if (x, y) in [(i - cell, j - cell), (i - cell, j + cell), (i + cell, j - cell),
                              (i + cell, j + cell)]:
                    continue
                # Skip the current cell
                if x == i and y == j:
                    continue
                # If any cell in the region has a value >= current cell, it's not a regional maximum
                if matrix[x][y] >= cell:
                    return False
        return True

    # Iterate over all cells to find regional maxima
    for i in range(rows):
        for j in range(cols):
            if is_regional_maximum(i, j):
                result.append([i, j])

    return result


# Example input
matrix = [
    [3, 0, 1],
    [2, 0, 0],
    [0, 0, 0],
]

# Output
print(find_regional_maxima(matrix))


#########################################################################

def difference_upper_lower(s: str) -> int:
    upper_count = 0
    lower_count = 0

    # Iterate through the string and count uppercase and lowercase letters
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    # Return the difference
    return abs(upper_count - lower_count)


# Example usage
input_string = "HelloWorld"
result = difference_upper_lower(input_string)
print(f"Difference of uppercase and lowercase letters: {result}")

#########################################################################

from collections import defaultdict


def bucket_with_max_files(commands):
    current_bucket = None
    bucket_files = defaultdict(int)

    for command in commands:
        if command.startswith("goto"):
            # Extract the bucket name from the "goto" command
            current_bucket = command.split(" ")[1]
        elif command.startswith("create") and current_bucket:
            # Extract the file name from the "create" command
            file_name = command.split(" ")[1]
            # Increment the file count for the current bucket
            bucket_files[current_bucket] += 1

    # Find the bucket with the maximum number of files
    max_bucket = max(bucket_files, key=bucket_files.get, default=None)

    return max_bucket


# Example usage
commands = ["goto Bucket_A", "create File_A", "create File_B", "goto Bucket_C", "create File_Y"]
result = bucket_with_max_files(commands)
print(f"The bucket with the maximum number of files is: {result}")

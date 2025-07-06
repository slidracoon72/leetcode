from typing import List


class Solution:
    # Using Counting Sort approach
    # Time Complexity: O(n), where n is the maximum position value in seats or students
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Determine the maximum position value in seats or students to size the count arrays
        max_index = max(max(seats), max(students)) + 1

        # Initialize count arrays to store the frequency of each position for seats and students
        count_seats = [0] * max_index
        count_students = [0] * max_index

        # Populate the count arrays with the number of students and seats at each position
        for seat, student in zip(seats, students):
            count_seats[seat] += 1
            count_students[student] += 1

        i, j = 0, 0  # Pointers for seats and students positions
        steps = 0  # To track the total number of moves
        remaining_to_move = len(students)  # The number of students left to move

        # Continue until all students have been moved
        while remaining_to_move:
            # Move the pointer i to the next seat position with available seats
            if count_seats[i] == 0:
                i += 1

            # Move the pointer j to the next student position with students to move
            if count_students[j] == 0:
                j += 1

            # If there are seats and students at positions i and j respectively
            if count_seats[i] and count_students[j]:
                # Calculate the steps needed to move a student from position j to position i
                steps += abs(i - j)

                # Update the count arrays after moving a student to a seat
                count_seats[i] -= 1
                count_students[j] -= 1

                # Decrement the number of students left to move
                remaining_to_move -= 1

        # Return the total number of moves required
        return steps

    # Using built-in Python sort function (Timsort)
    def minMovesToSeat1(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        steps = 0
        for i in range(len(students)):
            steps += abs(seats[i] - students[i])
        return steps

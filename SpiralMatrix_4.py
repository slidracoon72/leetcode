from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        # Create an empty matrix filled with -1
        matrix = [[-1] * n for _ in range(m)]

        # Define the boundaries of the matrix
        top, bottom = 0, m
        left, right = 0, n

        # Initialize the pointer to traverse the linked list
        current = head

        while left < right and top < bottom:
            # Fill the top row
            for i in range(left, right):
                if current:
                    matrix[top][i] = current.val
                    current = current.next
                else:
                    break
            top += 1

            # Fill the right column
            for i in range(top, bottom):
                if current:
                    matrix[i][right - 1] = current.val
                    current = current.next
                else:
                    break
            right -= 1

            # If only one row/column exists, break
            if not (left < right and top < bottom):
                break

            # Fill the bottom row
            for i in range(right - 1, left - 1, -1):
                if current:
                    matrix[bottom - 1][i] = current.val
                    current = current.next
                else:
                    break
            bottom -= 1

            # Fill the left column
            for i in range(bottom - 1, top - 1, -1):
                if current:
                    matrix[i][left] = current.val
                    current = current.next
                else:
                    break
            left += 1

        return matrix

from typing import List


# Dynamic Programming - Knapsack Problem
# Memoization (caching)
# Neetcode: https://www.youtube.com/watch?v=lFYPPPTp8qE
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # Memoization dictionary to store the minimum height of bookshelves
        # for each starting book index 'i'
        cache = {}

        def helper(i):
            # Base case: If we have considered all books, no more height needed
            if i == len(books):
                return 0

            # Check if the result for this starting index 'i' is already computed
            if i in cache:
                return cache[i]

            # Initialize the remaining width of the current shelf and the maximum height
            remaining_width = shelfWidth
            max_height = 0
            # Start with the maximum height being infinity (to find the minimum)
            cache[i] = float('inf')

            # Iterate through the books starting from index 'i'
            for j in range(i, len(books)):
                width, height = books[j]
                # If the book cannot fit on the current shelf, break the loop
                if remaining_width < width:
                    break
                # Update the remaining width of the shelf after placing the book
                remaining_width -= width
                # Update the maximum height of the current shelf
                max_height = max(max_height, height)
                # Recursively calculate the height needed for the rest of the books
                # and update the minimum height for the current index 'i'
                cache[i] = min(cache[i], helper(j + 1) + max_height)

            # Return the computed minimum height for the current starting index 'i'
            return cache[i]

        # Start the recursion from the first book
        return helper(0)

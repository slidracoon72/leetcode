import heapq


class Solution:
    # Time: O(n) where n=a+b+c, Space: (n) for res string
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max-heap with the negative counts (since Python heapq is a min-heap by default)
        heap = []
        if a > 0:
            heap.append([-a, "a"])
        if b > 0:
            heap.append([-b, "b"])
        if c > 0:
            heap.append([-c, "c"])
        heapq.heapify(heap)

        res = ""

        # Keep adding characters to the result string
        while heap:
            # Get the character with the highest frequency
            first = heapq.heappop(heap)

            # If the last two characters in the result are the same as the current one, we need to pick the next one
            if len(res) >= 2 and res[-1] == res[-2] == first[1]:
                if not heap:
                    break  # No other characters to use

                # Pick the second highest frequency character
                second = heapq.heappop(heap)
                res += second[1]
                second[0] += 1  # Decrease the count of the second character

                # Push the second character back into the heap if there are still more left
                if second[0] < 0:
                    heapq.heappush(heap, second)

                # Also push the first character back into the heap for later use
                heapq.heappush(heap, first)
            else:
                # Otherwise, we can safely use the most frequent character
                res += first[1]
                first[0] += 1  # Decrease the count of the first character

                # Push the first character back into the heap if there are still more left
                if first[0] < 0:
                    heapq.heappush(heap, first)

        return res

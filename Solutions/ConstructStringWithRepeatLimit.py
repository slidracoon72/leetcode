from collections import Counter
import heapq


class Solution:
    # Solved using Max-Heap
    # Time: O(nlogn), Space: O(n)
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Count the frequency of each character
        count = Counter(s)

        # Step 2: Use a max heap to store characters sorted by their ASCII values (descending)
        # We store (-ord(char), count) because heapq in Python implements a min-heap.
        maxHeap = [(-ord(char), cnt) for char, cnt in count.items()]
        heapq.heapify(maxHeap)  # Convert the list into a heap

        # Resultant list to store the final repeat-limited string
        res = []

        # Step 3: Build the repeat-limited string
        while maxHeap:
            # Pop the character with the largest ASCII value (lexicographically largest)
            char, cnt = heapq.heappop(maxHeap)
            char = chr(-char)  # Convert the negative ASCII value back to character

            # Append the current character to the result up to repeatLimit times
            cur_cnt = min(repeatLimit, cnt)  # Limit how many times the character can appear consecutively
            res.append(char * cur_cnt)

            # Calculate the remaining count of the current character
            remaining = cnt - cur_cnt

            # If there are still characters left and the heap is not empty
            if remaining and maxHeap:
                # Pop the next largest character (to break the consecutive repeat limit)
                next_char, next_cnt = heapq.heappop(maxHeap)
                next_char = chr(-next_char)

                # Append this character once to break the consecutive sequence
                res.append(next_char)
                next_cnt -= 1  # Decrement the count of the next character

                # If there are remaining next_char characters, push them back into the heap
                if next_cnt > 0:
                    heapq.heappush(maxHeap, (-ord(next_char), next_cnt))

                # Push the remaining count of the current character back into the heap
                heapq.heappush(maxHeap, (-ord(char), remaining))

        # Step 4: Combine the result list into the final string
        return "".join(res)


c = Solution()
s = "cczazcc"
repeatLimit = 3
print(c.repeatLimitedString(s, repeatLimit))

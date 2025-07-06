import heapq


class Solution:
    # My Solution
    # Time: O(n*logn), Space: O(n)
    def minimumPushes(self, word: str) -> int:
        # Create a dictionary to count occurrences of each character
        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)

        # Sort items by frequency in descending order; list returned
        sorted_items = sorted(count.items(), key=lambda x: -x[1])

        # Define segment sizes and their corresponding multipliers
        segment_sizes = [8, 8, 8, 2]  # Number of characters per segment (total 26 alphabets)
        multipliers = [1, 2, 3, 4]  # Multipliers for each segment

        # Initialize index and result accumulator
        index = 0
        res = 0

        # Loop through each segment and apply the multipliers
        for segment_size, multiplier in zip(segment_sizes, multipliers):
            for _ in range(segment_size):
                if index >= len(sorted_items):
                    break  # Stop if there are no more items to process
                key, value = sorted_items[index]
                res += value * multiplier  # Calculate contribution to result
                index += 1  # Move to the next item

        return res  # Return the total result

    # Neetcode: https://www.youtube.com/watch?v=gvaYi6X6SQw
    # Same logic as mine, code optimized
    # Time: O(n), Space: O(1)
    def minimumPushes_1(self, word: str) -> int:
        counts = [0] * 26
        for c in word:
            counts[ord(c) - ord('a')] += 1
        counts.sort(reverse=True)

        res = 0
        for i, count in enumerate(counts):
            res += count * (1 + i // 8)
        return res

    # Using Max-Heap
    def minimumPushes_2(self, word: str) -> int:
        # Initialize a list to count occurrences of each letter (26 letters in the alphabet)
        counts = [0] * 26

        # Count occurrences of each character in the input string
        for c in word:
            # Convert character to its corresponding index (0 for 'a', 1 for 'b', ..., 25 for 'z')
            index = ord(c) - ord('a')
            # Decrement the count for this character for max-heap
            # Value with most occurrences will have the max -ve value, thus it will be at top of the heap
            counts[index] -= 1

        # Convert the list of counts into a max-heap by negating the counts
        # Python's heapq module only supports min-heaps, so we use negative values to simulate a max-heap
        heapq.heapify(counts)

        # Initialize result accumulator and index counter
        res = 0
        i = 0

        # Process all elements in the heap
        while counts:
            # Pop the largest count from the heap (negate it back to positive)
            count = -heapq.heappop(counts)

            # Calculate the contribution to the result based on the segment index
            # (1 + i // 8) calculates the multiplier based on the segment position
            res += count * (1 + i // 8)

            # Increment the index counter
            i += 1

        return res


c = Solution()
word = "aabbccddeeffgghhiiiiii"
# word = 'xyzxyzxyzxyz'
# word = 'abcde'
print(c.minimumPushes(word))
print(c.minimumPushes_1(word))
print(c.minimumPushes_2(word))

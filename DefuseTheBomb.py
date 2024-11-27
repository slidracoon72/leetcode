from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N

        for i in range(N):
            if k > 0:
                for j in range(i + 1, i + 1 + k):
                    res[i] += code[j % N]
            elif k < 0:
                for j in range(i - 1, i - 1 - abs(k), -1):
                    res[i] += code[j % N]

        return res

    # Using Sliding Window - Most optimal
    def decrypt2(self, code: List[int], k: int) -> List[int]:
        N = len(code)  # Length of the input array
        res = [0] * N  # Initialize result array with zeros

        l = 0  # Left pointer for the sliding window
        cur_sum = 0  # Variable to keep track of the sum of the current window

        # Iterate over the indices considering the circular nature of the array
        for r in range(N + abs(k)):
            cur_sum += code[r % N]  # Add the current element to the sliding window sum

            # Shrink the window size if it exceeds |k|
            if r - l + 1 > abs(k):
                cur_sum -= code[l % N]  # Remove the element at the left of the window
                l = (l + 1) % N  # Move the left pointer to the right

            # When the window size equals |k|
            if r - l + 1 == abs(k):
                if k > 0:  # For positive k, assign the sum to the current left pointer index
                    res[(l - 1) % N] = cur_sum
                elif k < 0:  # For negative k, assign the sum to the index after the right pointer
                    res[(r + 1) % N] = cur_sum

        return res

    # Doubling the array to simulate a circular array
    def decrypt3(self, code: List[int], k: int) -> List[int]:
        temp = code + code
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            for i in range(len(code)):
                code[i] = sum(temp[i + 1:i + 1 + k])
            return code
        else:
            for i in range(len(code), len(temp)):
                code[i - len(code)] = sum(temp[i + k:i])
            return code

    # Similar as above, Using Sliding Window
    def decrypt4(self, code: List[int], k: int) -> List[int]:
        temp = code + code
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            cur = 0
            l = 0
            for r in range(1, len(temp)):
                cur += temp[r]
                if l < len(code) and r - l == k:
                    code[l] = cur
                    cur -= temp[l + 1]
                    l += 1
            return code
        else:
            for i in range(len(code), len(temp)):
                code[i - len(code)] = sum(temp[i + k:i])
            return code


c = Solution()
code = [2, 4, 9, 3]
k = -2
print(c.decrypt(code, k))

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        last_occurrence = {int(x): i for i, x in enumerate(num_list)}  # Store the last occurrence of each digit

        # Iterate over the digits of the number
        for i, digit in enumerate(num_list):
            # Check if there's a larger digit that occurs later in the number
            for d in range(9, int(digit), -1):  # Check from 9 down to (digit + 1)
                if last_occurrence.get(d, -1) > i:  # If there's a larger digit later
                    # Swap and return the new number
                    num_list[i], num_list[last_occurrence[d]] = num_list[last_occurrence[d]], num_list[i]
                    return int("".join(num_list))

        return num  # If no swap was made, return the original number


c = Solution()
print(c.maximumSwap(98368))

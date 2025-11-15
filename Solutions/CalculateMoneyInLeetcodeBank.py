class Solution:
    def totalMoney(self, n: int) -> int:
        # 'prev' keeps track of the previous Monday's starting deposit amount
        # 'cur' represents the current day's deposit amount (starting from 1)
        prev, cur = 0, 1

        total = 0  # Total money accumulated over 'n' days
        temp = 0  # Counter to track the number of days in the current week (1 to 7)

        # Iterate over 'n' days
        for _ in range(n):
            temp += 1  # Move to the next day of the week
            total += cur  # Add today's deposit amount to the total savings

            # If we’ve reached the end of the week (7 days)
            if temp == 7:
                temp = 0  # Reset the day counter for a new week
                cur = prev + 1  # Set next Monday’s starting deposit (1 more than previous Monday)
                prev += 1  # Update 'prev' for the next week's reference

            # Increment the deposit amount for the next day
            cur += 1

        # Return the total amount saved after 'n' days
        return total


c = Solution()
print(c.totalMoney(4))
print(c.totalMoney(10))
print(c.totalMoney(20))

from typing import List


# Neetcode: https://www.youtube.com/watch?v=2fN7uIgCIBA
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # Initialize current_time to keep track of the chef's timeline
        current_time = 0
        # Initialize total_wait to accumulate the total waiting time of all customers
        total_wait = 0

        # Iterate through each customer in the list
        for arrival, order in customers:
            wait = 0  # Initialize wait time for the current customer

            # If the chef is still busy when the customer arrives, calculate the wait time
            if current_time > arrival:
                wait = current_time - arrival
            else:
                # If the chef is idle, set the current_time to the customer's arrival time
                current_time = arrival

            # Add the order preparation time and wait time to the total waiting time
            total_wait += order + wait
            # Update the current_time to when the chef finishes the current order
            current_time += order

        # Calculate and return the average waiting time
        return total_wait / len(customers)


# Example usage:
c = Solution()
customers = [[1, 2], [2, 5], [4, 3]]
print(c.averageWaitingTime(customers))  # Output: 5.00000

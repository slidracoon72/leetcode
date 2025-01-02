import heapq
from collections import defaultdict
from typing import List


class Solution:
    # Question 1 - Count Triplets With Same First & Last Character
    # Time: O(n), Space: O(1)
    def countTriplets(self, s: str) -> int:
        if len(s) < 3:
            return 0

        count = 0
        s = s.lower()
        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                count += 1
        return count

    # Question 2 - Replace Every nth Consonant With Next Consonant
    # Time: O(len(message)), Space: O(len(message))
    def replaceWithNextConsonant(self, message: str, n: int) -> str:
        # Define consonants and create a mapping to their indices
        cons = "bcdfghjklmnpqrstvwxyz"
        ind_map = defaultdict(int)
        for i, c in enumerate(cons):
            ind_map[c] = i
            ind_map[c.upper()] = i  # Handle uppercase letters

        # Helper function to get the next consonant
        def next_consonant(c):
            if c.lower() not in ind_map:  # Non-consonants remain unchanged
                return c
            index = (ind_map[c.lower()] + 1) % len(cons)  # Wrap around at the end
            next_c = cons[index]
            return next_c if c.islower() else next_c.upper()

        # Replace every nth consonant in the message
        count = 0
        result = []
        for char in message:
            if char.lower() in ind_map:  # Check if the character is a consonant
                count += 1
                if count % n == 0:  # Replace nth consonant
                    result.append(next_consonant(char))
                else:
                    result.append(char)
            else:
                result.append(char)  # Non-consonants remain unchanged

        return ''.join(result)

    # Question 3 - Inventory Tracking System
    # Time: O(n * log k), Space: O(k * m)
    def inventoryTrackingSystem(self, logs: List[List[str]]) -> List[int]:
        # Dictionary to store inventory as a min-heap for each item
        inventory = defaultdict(list)

        # Tracker to monitor sold items and their prices
        sold_tracker = defaultdict(lambda: defaultdict(int))

        # List to store revenue from each "sell" transaction
        revenue = []

        # Process each transaction log
        for log in logs:
            transaction = log[0]

            if transaction == "supply":
                # "supply" transaction: Add item to inventory
                item, count, price = log[1], int(log[2]), int(log[3])
                # Push the item into the inventory heap with [price, count]
                heapq.heappush(inventory[item], [price, count])

            elif transaction == "sell":
                # "sell" transaction: Sell the requested quantity of an item
                item, count = log[1], int(log[2])
                total_revenue = 0  # To calculate total revenue for this transaction

                while count > 0:
                    # Get the cheapest available inventory for the item
                    price, available = heapq.heappop(inventory[item])

                    if available > count:
                        # If the available stock is more than requested
                        total_revenue += count * price  # Calculate revenue
                        sold_tracker[item][price] += count  # Track sold items
                        available -= count  # Update remaining stock
                        # Push the remaining stock back to the inventory
                        heapq.heappush(inventory[item], [price, available])
                        count = 0  # All requested items are sold
                    else:
                        # If the available stock is less than or equal to requested
                        total_revenue += available * price  # Calculate revenue
                        sold_tracker[item][price] += available  # Track sold items
                        count -= available  # Update remaining request

                # Append the revenue from this transaction to the result list
                revenue.append(total_revenue)

            elif transaction == "return":
                # "return" transaction: Return previously sold items to inventory
                item, count, sell_price, new_price = log[1], int(log[2]), int(log[3]), int(log[4])

                # Update the sold tracker to reflect the return
                sold_tracker[item][sell_price] -= count

                # Add the returned items back to inventory with the new price
                heapq.heappush(inventory[item], [new_price, count])

        # Return the list of revenues for all "sell" transactions
        return revenue


c = Solution()

# Q-1
s = "aXAccc"
print(c.countTriplets(s))
# Q-2
message = "CodeSignalWrttYD"
n = 3
print(c.replaceWithNextConsonant(message, n))
# Q-3
logs = [
    ["supply", "item1", "2", "100"],
    ["supply", "item2", "3", "60"],
    ["sell", "item1", "1"],
    ["sell", "item1", "1"],
    ["sell", "item2", "2"],
    ["return", "item2", "1", "60", "40"],
    ["sell", "item2", "1"],
    ["sell", "item2", "1"],
]
print(c.inventoryTrackingSystem(logs))

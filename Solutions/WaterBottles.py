# Time: O(logn)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Initialize the count of bottles drunk to the initial number of full bottles
        count = numBottles
        # Initialize the number of empty bottles to the initial number of full bottles
        empty_bottles = numBottles

        # Continue the loop as long as we have enough empty bottles to exchange for at least one full bottle
        while empty_bottles >= numExchange:
            # Calculate the number of new full bottles we get by exchanging empty bottles
            new_bottles = empty_bottles // numExchange
            # Update the number of empty bottles to the remainder after exchanging, plus the new full bottles
            empty_bottles = (empty_bottles % numExchange) + new_bottles
            # Add the new full bottles to the count of total bottles drunk
            count += new_bottles

        # Return the total count of bottles drunk.
        return count


c = Solution()
numBottles = 15
numExchange = 4
print(c.numWaterBottles(numBottles, numExchange))

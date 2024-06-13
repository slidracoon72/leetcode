from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # Create an empty stack to store asteroids

        # Iterate through each asteroid in the input list
        for x in asteroids:
            if x > 0:  # If the asteroid is moving to the right
                stack.append(x)  # Add it to the stack
            else:  # If the asteroid is moving to the left
                # Check for collisions with asteroids moving to the right
                while stack and stack[-1] > 0:
                    if stack[-1] + x == 0:  # If the sizes of the asteroids are equal
                        stack.pop()  # Both asteroids explode
                        break
                    elif stack[-1] + x > 0:  # If the asteroid moving to the left is smaller
                        break  # The asteroid moving to the left explodes
                    else:  # If the asteroid moving to the right is smaller
                        stack.pop()  # The asteroid moving to the right explodes
                else:
                    stack.append(x)  # If there's no collision, add the asteroid to the stack

        return stack  # Return the remaining asteroids after all collisions


asteroids = [5, 10, -5]
# asteroids = [8, -8]
# asteroids = [10, 2, -5]
c = Solution()
print(c.asteroidCollision(asteroids))

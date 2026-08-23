from typing import List


class Solution:
    # Time: O(n) — each asteroid is pushed onto the stack at most once and
    #       popped at most once, so total work across all iterations is
    #       linear despite the nested while loop.
    # Space: O(n) — the stack can hold up to n asteroids in the worst case
    #        (e.g. all asteroids moving in the same direction, no collisions).
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # stack holds asteroids that have survived collisions so far

        for a in asteroids:
            # A collision only happens when the current asteroid is moving
            # left (a < 0) and the top of the stack is moving right (stack[-1] > 0) —
            # that's the only case where two asteroids are moving toward each other.
            while stack and a < 0 and stack[-1] > 0:
                diff = stack[-1] + a  # compare sizes: negative means 'a' wins, positive means stack top wins

                if diff < 0:
                    # stack[-1] (moving right) is smaller and gets destroyed;
                    # 'a' survives and keeps moving left, so re-check against
                    # the next asteroid down the stack
                    stack.pop()
                elif diff > 0:
                    # 'a' (moving left) is smaller and gets destroyed;
                    # stack[-1] survives untouched
                    a = 0
                else:
                    # equal size: both asteroids destroy each other
                    stack.pop()
                    a = 0

            # only push 'a' if it survived all collisions (a == 0 means destroyed)
            if a:
                stack.append(a)

        return stack


class Solution1:
    # Stack
    # Time: O(n), Space: O(n)
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

    def asteroidCollision1(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop()

                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] == abs(a):
                    stack.pop()
        return stack


asteroids = [5, 10, -5]
# asteroids = [8, -8]
# asteroids = [10, 2, -5]
c = Solution()
print(c.asteroidCollision(asteroids))

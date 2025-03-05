# LC-1415: The k-th Lexicographical String of All Happy Strings of Length n


class Solution:
    # Recursive Backtracking - Using Array
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []

        # Recursive backtracking function to generate happy strings
        def backtrack(curr: str):
            # Stop recursion early if we have already found k happy strings
            if len(happy_strings) == k:
                return

            # If word of length 'n' is formed
            if len(curr) == n:
                happy_strings.append(curr)
                return

            for ch in "abc":
                if not curr or curr[-1] != ch:  # Ensure consecutive characters are different
                    backtrack(curr + ch)

        backtrack("")

        # Return the k-th happy string if it exists
        return happy_strings[-1] if len(happy_strings) == k else ""

    # Recursive Backtracking - Without Using Array (More Optimized)
    def getHappyString1(self, n: int, k: int) -> str:
        self.count = 0  # Tracks how many happy strings have been generated so far
        self.result = ""  # Stores the k-th happy string when found

        def backtrack(curr: str):
            # Stop recursion if we've found the k-th happy string
            if self.count == k:
                return

            # If we reach the required length, increase count and check if it's the k-th
            if len(curr) == n:
                self.count += 1
                if self.count == k:
                    self.result = curr
                return

            for ch in "abc":
                if not curr or curr[-1] != ch:  # Ensure consecutive characters are different
                    backtrack(curr + ch)
                    if self.count == k:  # Early exit condition to avoid unnecessary recursion
                        return

        backtrack("")
        return self.result if self.result else ""


c = Solution()
print(c.getHappyString(3, 3))
print(c.getHappyString(3, 9))

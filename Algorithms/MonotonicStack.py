from typing import List, Optional, Tuple
from collections import deque


class MonotonicStack:
    """
    Comprehensive Monotonic Stack implementation with common patterns and applications.
    
    A Monotonic Stack is a stack that maintains either strictly increasing or decreasing
    order of elements. It's particularly useful for problems involving:
    - Next greater/smaller element
    - Largest rectangle in histogram
    - Stock span problem
    - Rain water trapping
    - Sliding window maximum/minimum
    
    Time Complexity: O(n) for most operations
    Space Complexity: O(n)
    """
    
    def next_greater_element(self, nums: List[int]) -> List[int]:
        """
        Find next greater element for each element.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            nums: Input array
            
        Returns:
            Array where result[i] is next greater element for nums[i], -1 if none
        """
        n = len(nums)
        result = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        
        return result
    
    def next_greater_element_ii(self, nums: List[int]) -> List[int]:
        """
        Find next greater element in circular array.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            nums: Input circular array
            
        Returns:
            Array where result[i] is next greater element for nums[i], -1 if none
        """
        n = len(nums)
        result = [-1] * n
        stack = []
        
        # Process array twice to handle circular nature
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                result[stack.pop()] = nums[idx]
            stack.append(idx)
        
        return result
    
    def next_smaller_element(self, nums: List[int]) -> List[int]:
        """
        Find next smaller element for each element.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            nums: Input array
            
        Returns:
            Array where result[i] is next smaller element for nums[i], -1 if none
        """
        n = len(nums)
        result = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        
        return result
    
    def previous_greater_element(self, nums: List[int]) -> List[int]:
        """
        Find previous greater element for each element.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            nums: Input array
            
        Returns:
            Array where result[i] is previous greater element for nums[i], -1 if none
        """
        n = len(nums)
        result = [-1] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        
        return result
    
    def previous_smaller_element(self, nums: List[int]) -> List[int]:
        """
        Find previous smaller element for each element.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            nums: Input array
            
        Returns:
            Array where result[i] is previous smaller element for nums[i], -1 if none
        """
        n = len(nums)
        result = [-1] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        
        return result
    
    def largest_rectangle_in_histogram(self, heights: List[int]) -> int:
        """
        Find largest rectangle area in histogram.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            heights: Array of histogram heights
            
        Returns:
            Maximum rectangle area
        """
        if not heights:
            return 0
        
        max_area = 0
        stack = []
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        # Process remaining elements in stack
        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area
    
    def maximal_rectangle(self, matrix: List[List[str]]) -> int:
        """
        Find maximal rectangle in binary matrix.
        
        Time Complexity: O(mn)
        Space Complexity: O(n)
        
        Args:
            matrix: Binary matrix
            
        Returns:
            Maximum rectangle area
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for i in range(m):
            # Update heights
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Find largest rectangle in current histogram
            max_area = max(max_area, self.largest_rectangle_in_histogram(heights))
        
        return max_area
    
    def stock_span_problem(self, prices: List[int]) -> List[int]:
        """
        Calculate stock span for each day.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            prices: Array of stock prices
            
        Returns:
            Array where result[i] is span for day i
        """
        n = len(prices)
        result = [1] * n
        stack = []
        
        for i in range(n):
            while stack and prices[stack[-1]] <= prices[i]:
                result[i] += result[stack.pop()]
            stack.append(i)
        
        return result
    
    def trapping_rain_water(self, height: List[int]) -> int:
        """
        Calculate trapped rain water.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            height: Array of heights
            
        Returns:
            Total trapped water
        """
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        # Calculate left max heights
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        # Calculate right max heights
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Calculate trapped water
        total_water = 0
        for i in range(n):
            water = min(left_max[i], right_max[i]) - height[i]
            total_water += max(0, water)
        
        return total_water
    
    def trapping_rain_water_stack(self, height: List[int]) -> int:
        """
        Calculate trapped rain water using stack.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            height: Array of heights
            
        Returns:
            Total trapped water
        """
        if not height:
            return 0
        
        total_water = 0
        stack = []
        
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                
                if not stack:
                    break
                
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                total_water += distance * bounded_height
            
            stack.append(i)
        
        return total_water
    
    def sliding_window_maximum(self, nums: List[int], k: int) -> List[int]:
        """
        Find maximum element in each sliding window.
        
        Time Complexity: O(n)
        Space Complexity: O(k)
        
        Args:
            nums: Input array
            k: Window size
            
        Returns:
            Array of maximum elements for each window
        """
        if not nums or k == 0:
            return []
        
        result = []
        dq = deque()  # Store indices
        
        for i in range(len(nums)):
            # Remove elements outside current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # Add maximum for current window
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
    
    def sliding_window_minimum(self, nums: List[int], k: int) -> List[int]:
        """
        Find minimum element in each sliding window.
        
        Time Complexity: O(n)
        Space Complexity: O(k)
        
        Args:
            nums: Input array
            k: Window size
            
        Returns:
            Array of minimum elements for each window
        """
        if not nums or k == 0:
            return []
        
        result = []
        dq = deque()  # Store indices
        
        for i in range(len(nums)):
            # Remove elements outside current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove larger elements from back
            while dq and nums[dq[-1]] > nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # Add minimum for current window
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
    
    def remove_k_digits(self, num: str, k: int) -> str:
        """
        Remove k digits to form smallest number.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            num: Input number as string
            k: Number of digits to remove
            
        Returns:
            Smallest number after removing k digits
        """
        if k >= len(num):
            return "0"
        
        stack = []
        
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Remove remaining k digits from end
        while k > 0:
            stack.pop()
            k -= 1
        
        # Remove leading zeros
        result = ''.join(stack).lstrip('0')
        return result if result else "0"
    
    def asteroid_collision(self, asteroids: List[int]) -> List[int]:
        """
        Simulate asteroid collisions.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            asteroids: Array of asteroid sizes (positive = right, negative = left)
            
        Returns:
            Array of remaining asteroids
        """
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)
        
        return stack
    
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        """
        Find number of days to wait for warmer temperature.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            temperatures: Array of daily temperatures
            
        Returns:
            Array where result[i] is days to wait for warmer temperature
        """
        n = len(temperatures)
        result = [0] * n
        stack = []
        
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack.pop()] = i - stack[-1] if stack else i
            stack.append(i)
        
        return result
    
    def validate_stack_sequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Validate if popped sequence can be obtained from pushed sequence.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            pushed: Sequence of pushed elements
            popped: Sequence of popped elements
            
        Returns:
            True if valid, False otherwise
        """
        stack = []
        pop_index = 0
        
        for num in pushed:
            stack.append(num)
            
            while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        
        return pop_index == len(popped)


# Example usage and testing
if __name__ == "__main__":
    print("Monotonic Stack Demo:")
    print("====================")
    
    ms = MonotonicStack()
    
    # Next Greater Element
    nums = [4, 5, 2, 10, 8]
    next_greater = ms.next_greater_element(nums)
    print(f"Next greater elements for {nums}: {next_greater}")
    
    # Next Greater Element II (Circular)
    next_greater_circular = ms.next_greater_element_ii(nums)
    print(f"Next greater elements (circular) for {nums}: {next_greater_circular}")
    
    # Next Smaller Element
    next_smaller = ms.next_smaller_element(nums)
    print(f"Next smaller elements for {nums}: {next_smaller}")
    
    # Previous Greater Element
    prev_greater = ms.previous_greater_element(nums)
    print(f"Previous greater elements for {nums}: {prev_greater}")
    
    # Previous Smaller Element
    prev_smaller = ms.previous_smaller_element(nums)
    print(f"Previous smaller elements for {nums}: {prev_smaller}")
    
    # Largest Rectangle in Histogram
    heights = [2, 1, 5, 6, 2, 3]
    max_area = ms.largest_rectangle_in_histogram(heights)
    print(f"Largest rectangle area in {heights}: {max_area}")
    
    # Maximal Rectangle
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    max_rect = ms.maximal_rectangle(matrix)
    print(f"Maximal rectangle area: {max_rect}")
    
    # Stock Span Problem
    prices = [100, 80, 60, 70, 60, 75, 85]
    spans = ms.stock_span_problem(prices)
    print(f"Stock spans for {prices}: {spans}")
    
    # Trapping Rain Water
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    water = ms.trapping_rain_water(height)
    print(f"Trapped water for {height}: {water}")
    
    water_stack = ms.trapping_rain_water_stack(height)
    print(f"Trapped water (stack method): {water_stack}")
    
    # Sliding Window Maximum
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    window_max = ms.sliding_window_maximum(nums, k)
    print(f"Sliding window maximum for {nums} with k={k}: {window_max}")
    
    # Sliding Window Minimum
    window_min = ms.sliding_window_minimum(nums, k)
    print(f"Sliding window minimum for {nums} with k={k}: {window_min}")
    
    # Remove K Digits
    num = "1432219"
    k = 3
    smallest = ms.remove_k_digits(num, k)
    print(f"Smallest number after removing {k} digits from {num}: {smallest}")
    
    # Asteroid Collision
    asteroids = [5, 10, -5]
    remaining = ms.asteroid_collision(asteroids)
    print(f"Remaining asteroids after collision {asteroids}: {remaining}")
    
    # Daily Temperatures
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    days = ms.daily_temperatures(temperatures)
    print(f"Days to wait for warmer temperature {temperatures}: {days}")
    
    # Validate Stack Sequences
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    is_valid = ms.validate_stack_sequences(pushed, popped)
    print(f"Stack sequence {pushed} -> {popped} is valid: {is_valid}")
    
    # Performance comparison
    print("\n" + "="*50)
    print("Performance Comparison:")
    print("="*50)
    
    import time
    
    # Test with large array
    n = 10000
    large_nums = list(range(n))
    
    start = time.time()
    next_greater_large = ms.next_greater_element(large_nums)
    stack_time = time.time() - start
    
    start = time.time()
    # Naive approach
    naive_result = []
    for i in range(n):
        found = False
        for j in range(i + 1, n):
            if large_nums[j] > large_nums[i]:
                naive_result.append(large_nums[j])
                found = True
                break
        if not found:
            naive_result.append(-1)
    naive_time = time.time() - start
    
    print(f"Monotonic stack time: {stack_time:.4f}s")
    print(f"Naive approach time: {naive_time:.4f}s")
    print(f"Speedup: {naive_time/stack_time:.2f}x") 
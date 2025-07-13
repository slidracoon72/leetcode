from typing import List, Optional, Callable
import math


class BinarySearch:
    """
    Comprehensive Binary Search implementation with various patterns and applications.
    
    Binary Search is a divide-and-conquer algorithm that works on sorted arrays.
    It repeatedly divides the search interval in half, making it very efficient.
    
    Time Complexity: O(log n) for most operations
    Space Complexity: O(1) for iterative, O(log n) for recursive
    """
    
    @staticmethod
    def binary_search_iterative(arr: List[int], target: int) -> int:
        """
        Standard binary search to find target in sorted array.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            arr: Sorted array to search in
            target: Value to find
            
        Returns:
            Index of target if found, -1 otherwise
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # Prevents integer overflow
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    @staticmethod
    def binary_search_recursive(arr: List[int], target: int) -> int:
        """
        Recursive binary search implementation.
        
        Time Complexity: O(log n)
        Space Complexity: O(log n) for recursion stack
        
        Args:
            arr: Sorted array to search in
            target: Value to find
            
        Returns:
            Index of target if found, -1 otherwise
        """
        def search(left: int, right: int) -> int:
            if left > right:
                return -1
            
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return search(mid + 1, right)
            else:
                return search(left, mid - 1)
        
        return search(0, len(arr) - 1)
    
    @staticmethod
    def find_first_occurrence(arr: List[int], target: int) -> int:
        """
        Find the first occurrence of target in sorted array (with duplicates).
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            arr: Sorted array with possible duplicates
            target: Value to find
            
        Returns:
            Index of first occurrence, -1 if not found
        """
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                result = mid
                right = mid - 1  # Continue searching left half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    @staticmethod
    def find_last_occurrence(arr: List[int], target: int) -> int:
        """
        Find the last occurrence of target in sorted array (with duplicates).
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            arr: Sorted array with possible duplicates
            target: Value to find
            
        Returns:
            Index of last occurrence, -1 if not found
        """
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                result = mid
                left = mid + 1  # Continue searching right half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    @staticmethod
    def find_insert_position(arr: List[int], target: int) -> int:
        """
        Find the position where target should be inserted to maintain sorted order.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            arr: Sorted array
            target: Value to insert
            
        Returns:
            Index where target should be inserted
        """
        left, right = 0, len(arr)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    @staticmethod
    def find_peak_element(arr: List[int]) -> int:
        """
        Find a peak element in array (element greater than its neighbors).
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            arr: Array where arr[i] != arr[i+1] for all valid i
            
        Returns:
            Index of a peak element
        """
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left
    
    @staticmethod
    def find_min_in_rotated_sorted(arr: List[int]) -> int:
        """
        Find minimum element in rotated sorted array.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            arr: Rotated sorted array
            
        Returns:
            Index of minimum element
        """
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    @staticmethod
    def search_in_rotated_sorted(arr: List[int], target: int) -> int:
        """
        Search for target in rotated sorted array.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            arr: Rotated sorted array
            target: Value to find
            
        Returns:
            Index of target if found, -1 otherwise
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                return mid
            
            # Check if left half is sorted
            if arr[left] <= arr[mid]:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
    
    @staticmethod
    def find_kth_smallest(arr: List[int], k: int) -> int:
        """
        Find kth smallest element in unsorted array using binary search on answer.
        
        Time Complexity: O(n log M) where M is the range of values
        Space Complexity: O(1)
        
        Args:
            arr: Unsorted array
            k: kth smallest element to find (1-indexed)
            
        Returns:
            kth smallest element
        """
        def count_less_equal(mid: int) -> int:
            count = 0
            for num in arr:
                if num <= mid:
                    count += 1
            return count
        
        left, right = min(arr), max(arr)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    @staticmethod
    def sqrt(x: int) -> int:
        """
        Find integer square root of x using binary search.
        
        Time Complexity: O(log x)
        Space Complexity: O(1)
        
        Args:
            x: Non-negative integer
            
        Returns:
            Integer square root of x
        """
        if x <= 1:
            return x
        
        left, right = 1, x
        
        while left < right:
            mid = left + (right - left) // 2
            
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        
        return left - 1
    
    @staticmethod
    def capacity_to_ship_packages(weights: List[int], days: int) -> int:
        """
        Find minimum capacity to ship packages within given days.
        
        Time Complexity: O(n log M) where M is sum of weights
        Space Complexity: O(1)
        
        Args:
            weights: List of package weights
            days: Number of days to ship all packages
            
        Returns:
            Minimum capacity needed
        """
        def can_ship(capacity: int) -> bool:
            current_weight = 0
            days_needed = 1
            
            for weight in weights:
                if weight > capacity:
                    return False
                
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = weight
                else:
                    current_weight += weight
                
                if days_needed > days:
                    return False
            
            return True
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
    @staticmethod
    def split_array_largest_sum(nums: List[int], k: int) -> int:
        """
        Split array into k subarrays to minimize the largest sum.
        
        Time Complexity: O(n log M) where M is sum of array
        Space Complexity: O(1)
        
        Args:
            nums: Array of integers
            k: Number of subarrays to split into
            
        Returns:
            Minimum largest sum among subarrays
        """
        def can_split(max_sum: int) -> bool:
            current_sum = 0
            subarrays = 1
            
            for num in nums:
                if num > max_sum:
                    return False
                
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                else:
                    current_sum += num
                
                if subarrays > k:
                    return False
            
            return True
        
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
    @staticmethod
    def binary_search_on_answer(func: Callable[[int], bool], left: int, right: int) -> int:
        """
        Generic binary search on answer space.
        
        Time Complexity: O(log(right - left)) * O(func)
        Space Complexity: O(1)
        
        Args:
            func: Function that returns True/False for a given value
            left: Left boundary of search space
            right: Right boundary of search space
            
        Returns:
            Smallest value for which func returns True
        """
        while left < right:
            mid = left + (right - left) // 2
            
            if func(mid):
                right = mid
            else:
                left = mid + 1
        
        return left


class BinarySearchApplications:
    """
    Common applications and problems solved using binary search.
    """
    
    @staticmethod
    def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
        """
        LeetCode 167: Two Sum II - Input Array Is Sorted
        Find two numbers that add up to target in sorted array.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            numbers: Sorted array
            target: Target sum
            
        Returns:
            Indices of two numbers (1-indexed)
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []
    
    @staticmethod
    def median_of_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
        """
        LeetCode 4: Median of Two Sorted Arrays
        Find median of two sorted arrays.
        
        Time Complexity: O(log(min(m, n)))
        Space Complexity: O(1)
        
        Args:
            nums1: First sorted array
            nums2: Second sorted array
            
        Returns:
            Median of the two arrays
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition_x = (left + right) // 2
            partition_y = (m + n + 1) // 2 - partition_x
            
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]
            
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]
            
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (m + n) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                right = partition_x - 1
            else:
                left = partition_x + 1
        
        return 0.0


# Example usage and testing
if __name__ == "__main__":
    print("Binary Search Demo:")
    print("==================")
    
    # Test data
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    arr_with_duplicates = [1, 2, 2, 2, 3, 4, 4, 5, 6]
    rotated_arr = [4, 5, 6, 7, 0, 1, 2]
    
    bs = BinarySearch()
    
    # Standard binary search
    print(f"Array: {arr}")
    print(f"Search 7: {bs.binary_search_iterative(arr, 7)}")
    print(f"Search 10: {bs.binary_search_iterative(arr, 10)}")
    print(f"Search 7 (recursive): {bs.binary_search_recursive(arr, 7)}")
    
    # First and last occurrence
    print(f"\nArray with duplicates: {arr_with_duplicates}")
    print(f"First occurrence of 2: {bs.find_first_occurrence(arr_with_duplicates, 2)}")
    print(f"Last occurrence of 2: {bs.find_last_occurrence(arr_with_duplicates, 2)}")
    print(f"First occurrence of 4: {bs.find_first_occurrence(arr_with_duplicates, 4)}")
    
    # Insert position
    print(f"\nInsert position for 8 in {arr}: {bs.find_insert_position(arr, 8)}")
    print(f"Insert position for 2 in {arr}: {bs.find_insert_position(arr, 2)}")
    
    # Peak element
    peak_arr = [1, 3, 5, 4, 2]
    print(f"\nPeak element in {peak_arr}: {bs.find_peak_element(peak_arr)}")
    
    # Rotated sorted array
    print(f"\nRotated array: {rotated_arr}")
    print(f"Minimum element: {bs.find_min_in_rotated_sorted(rotated_arr)}")
    print(f"Search 0: {bs.search_in_rotated_sorted(rotated_arr, 0)}")
    print(f"Search 3: {bs.search_in_rotated_sorted(rotated_arr, 3)}")
    
    # Kth smallest
    unsorted_arr = [3, 2, 1, 5, 6, 4]
    print(f"\nKth smallest in {unsorted_arr}")
    for k in range(1, 7):
        print(f"{k}th smallest: {bs.find_kth_smallest(unsorted_arr, k)}")
    
    # Square root
    print(f"\nSquare root of 16: {bs.sqrt(16)}")
    print(f"Square root of 8: {bs.sqrt(8)}")
    
    # Applications
    print("\n" + "="*50)
    print("Binary Search Applications:")
    print("="*50)
    
    # Two Sum Sorted
    sorted_nums = [2, 7, 11, 15]
    target = 9
    result = BinarySearchApplications.two_sum_sorted(sorted_nums, target)
    print(f"Two sum {target} in {sorted_nums}: {result}")
    
    # Median of two sorted arrays
    nums1 = [1, 3]
    nums2 = [2]
    median = BinarySearchApplications.median_of_two_sorted_arrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2}: {median}")
    
    # Capacity to ship packages
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    capacity = bs.capacity_to_ship_packages(weights, days)
    print(f"Minimum capacity to ship {weights} in {days} days: {capacity}")
    
    # Split array largest sum
    nums = [7, 2, 5, 10, 8]
    k = 2
    largest_sum = bs.split_array_largest_sum(nums, k)
    print(f"Minimum largest sum when splitting {nums} into {k} parts: {largest_sum}")
    
    # Generic binary search on answer
    def is_square_root_less_than_5(x):
        return x * x >= 25
    
    result = bs.binary_search_on_answer(is_square_root_less_than_5, 0, 10)
    print(f"Smallest number whose square is >= 25: {result}") 
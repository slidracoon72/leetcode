from typing import List, Optional, Tuple
from collections import defaultdict


class TwoPointers:
    """
    Comprehensive Two Pointers implementation with various patterns and applications.
    
    Two Pointers is a technique that uses two pointers to solve problems efficiently.
    Common patterns include:
    - Sliding Window
    - Fast/Slow Pointers (Floyd's Cycle Detection)
    - Left/Right Pointers
    - Three Pointers
    
    Time Complexity: Usually O(n) for most problems
    Space Complexity: Usually O(1) for most problems
    """
    
    @staticmethod
    def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
        """
        Two Sum II - Input Array Is Sorted (LeetCode 167)
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
    def three_sum(nums: List[int]) -> List[List[int]]:
        """
        3Sum (LeetCode 15)
        Find all unique triplets that sum to zero.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1) excluding output space
        
        Args:
            nums: Array of integers
            
        Returns:
            List of unique triplets that sum to zero
        """
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
    
    @staticmethod
    def container_with_most_water(height: List[int]) -> int:
        """
        Container With Most Water (LeetCode 11)
        Find two lines that together with x-axis forms a container that holds maximum water.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            height: Array of heights
            
        Returns:
            Maximum area of water that can be contained
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
    @staticmethod
    def remove_duplicates_from_sorted_array(nums: List[int]) -> int:
        """
        Remove Duplicates from Sorted Array (LeetCode 26)
        Remove duplicates in-place and return new length.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: Sorted array with duplicates
            
        Returns:
            New length of array after removing duplicates
        """
        if not nums:
            return 0
        
        write_index = 1
        
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        return write_index
    
    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        """
        Remove Element (LeetCode 27)
        Remove all instances of val in-place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: Array of integers
            val: Value to remove
            
        Returns:
            New length of array after removing val
        """
        write_index = 0
        
        for read_index in range(len(nums)):
            if nums[read_index] != val:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        return write_index
    
    @staticmethod
    def move_zeroes(nums: List[int]) -> None:
        """
        Move Zeroes (LeetCode 283)
        Move all zeros to the end while maintaining relative order of non-zero elements.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: Array of integers
        """
        write_index = 0
        
        for read_index in range(len(nums)):
            if nums[read_index] != 0:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        # Fill remaining positions with zeros
        while write_index < len(nums):
            nums[write_index] = 0
            write_index += 1
    
    @staticmethod
    def reverse_string(s: List[str]) -> None:
        """
        Reverse String (LeetCode 344)
        Reverse string in-place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            s: List of characters
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    @staticmethod
    def valid_palindrome(s: str) -> bool:
        """
        Valid Palindrome (LeetCode 125)
        Check if string is palindrome, ignoring non-alphanumeric characters.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            s: Input string
            
        Returns:
            True if palindrome, False otherwise
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    @staticmethod
    def is_subsequence(s: str, t: str) -> bool:
        """
        Is Subsequence (LeetCode 392)
        Check if s is subsequence of t.
        
        Time Complexity: O(n) where n is length of t
        Space Complexity: O(1)
        
        Args:
            s: Subsequence to check
            t: Target string
            
        Returns:
            True if s is subsequence of t, False otherwise
        """
        if not s:
            return True
        
        s_index = 0
        
        for char in t:
            if s_index < len(s) and s[s_index] == char:
                s_index += 1
                if s_index == len(s):
                    return True
        
        return False
    
    @staticmethod
    def linked_list_cycle_detection(head) -> bool:
        """
        Linked List Cycle (LeetCode 141)
        Detect if linked list has a cycle using Floyd's Cycle Detection.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            head: Head of linked list
            
        Returns:
            True if cycle exists, False otherwise
        """
        if not head or not head.next:
            return False
        
        slow, fast = head, head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
    
    @staticmethod
    def find_duplicate_number(nums: List[int]) -> int:
        """
        Find the Duplicate Number (LeetCode 287)
        Find duplicate number in array using Floyd's Cycle Detection.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: Array with one duplicate
            
        Returns:
            Duplicate number
        """
        slow, fast = nums[0], nums[0]
        
        # Find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
    
    @staticmethod
    def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
        """
        Sliding Window Maximum (LeetCode 239)
        Find maximum element in each sliding window of size k.
        
        Time Complexity: O(n)
        Space Complexity: O(k)
        
        Args:
            nums: Array of integers
            k: Window size
            
        Returns:
            List of maximum elements for each window
        """
        from collections import deque
        
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
    
    @staticmethod
    def minimum_window_substring(s: str, t: str) -> str:
        """
        Minimum Window Substring (LeetCode 76)
        Find minimum window in s that contains all characters in t.
        
        Time Complexity: O(n)
        Space Complexity: O(k) where k is unique characters in t
        
        Args:
            s: Source string
            t: Target string
            
        Returns:
            Minimum window substring
        """
        if not s or not t:
            return ""
        
        # Count characters in t
        target_count = defaultdict(int)
        for char in t:
            target_count[char] += 1
        
        required = len(target_count)
        formed = 0
        window_count = defaultdict(int)
        
        left, right = 0, 0
        min_len = float('inf')
        min_start = 0
        
        while right < len(s):
            char = s[right]
            window_count[char] += 1
            
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            
            # Try to minimize window
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return s[min_start:min_start + min_len] if min_len != float('inf') else ""
    
    @staticmethod
    def longest_substring_without_repeating_characters(s: str) -> int:
        """
        Longest Substring Without Repeating Characters (LeetCode 3)
        Find length of longest substring without repeating characters.
        
        Time Complexity: O(n)
        Space Complexity: O(min(m, n)) where m is charset size
        
        Args:
            s: Input string
            
        Returns:
            Length of longest substring without repeating characters
        """
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    @staticmethod
    def longest_repeating_character_replacement(s: str, k: int) -> int:
        """
        Longest Repeating Character Replacement (LeetCode 424)
        Find longest substring that can be made by replacing k characters.
        
        Time Complexity: O(n)
        Space Complexity: O(1) since we have fixed charset
        
        Args:
            s: Input string
            k: Number of characters that can be replaced
            
        Returns:
            Length of longest substring
        """
        count = defaultdict(int)
        left = 0
        max_count = 0
        max_length = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])
            
            # If window size - max_count > k, we need to shrink window
            if right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    @staticmethod
    def merge_sorted_array(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge Sorted Array (LeetCode 88)
        Merge nums2 into nums1 in-place.
        
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        
        Args:
            nums1: First sorted array with extra space
            m: Number of elements in nums1
            nums2: Second sorted array
            n: Number of elements in nums2
        """
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # Copy remaining elements from nums2
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
    
    @staticmethod
    def sort_colors(nums: List[int]) -> None:
        """
        Sort Colors (LeetCode 75)
        Sort array containing only 0, 1, 2 in-place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: Array containing only 0, 1, 2
        """
        left, mid, right = 0, 0, len(nums) - 1
        
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1


# Example usage and testing
if __name__ == "__main__":
    print("Two Pointers Demo:")
    print("==================")
    
    tp = TwoPointers()
    
    # Two Sum Sorted
    numbers = [2, 7, 11, 15]
    target = 9
    result = tp.two_sum_sorted(numbers, target)
    print(f"Two sum {target} in {numbers}: {result}")
    
    # Three Sum
    nums = [-1, 0, 1, 2, -1, -4]
    triplets = tp.three_sum(nums)
    print(f"Three sum zero in {nums}: {triplets}")
    
    # Container with most water
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_area = tp.container_with_most_water(height)
    print(f"Max water container area for {height}: {max_area}")
    
    # Remove duplicates
    arr = [1, 1, 2, 2, 3, 4, 4, 5]
    new_length = tp.remove_duplicates_from_sorted_array(arr)
    print(f"Array after removing duplicates: {arr[:new_length]}")
    
    # Remove element
    arr = [3, 2, 2, 3]
    val = 3
    new_length = tp.remove_element(arr, val)
    print(f"Array after removing {val}: {arr[:new_length]}")
    
    # Move zeroes
    arr = [0, 1, 0, 3, 12]
    tp.move_zeroes(arr)
    print(f"Array after moving zeroes: {arr}")
    
    # Reverse string
    s = list("hello")
    tp.reverse_string(s)
    print(f"Reversed string: {''.join(s)}")
    
    # Valid palindrome
    test_str = "A man, a plan, a canal: Panama"
    is_palindrome = tp.valid_palindrome(test_str)
    print(f"'{test_str}' is palindrome: {is_palindrome}")
    
    # Is subsequence
    s, t = "abc", "ahbgdc"
    is_subseq = tp.is_subsequence(s, t)
    print(f"'{s}' is subsequence of '{t}': {is_subseq}")
    
    # Find duplicate number
    nums = [1, 3, 4, 2, 2]
    duplicate = tp.find_duplicate_number(nums)
    print(f"Duplicate number in {nums}: {duplicate}")
    
    # Sliding window maximum
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    max_window = tp.sliding_window_maximum(nums, k)
    print(f"Sliding window maximum for {nums} with k={k}: {max_window}")
    
    # Minimum window substring
    s, t = "ADOBECODEBANC", "ABC"
    min_window = tp.minimum_window_substring(s, t)
    print(f"Minimum window of '{t}' in '{s}': '{min_window}'")
    
    # Longest substring without repeating characters
    s = "abcabcbb"
    max_length = tp.longest_substring_without_repeating_characters(s)
    print(f"Longest substring without repeating in '{s}': {max_length}")
    
    # Longest repeating character replacement
    s, k = "AABABBA", 1
    max_length = tp.longest_repeating_character_replacement(s, k)
    print(f"Longest repeating character replacement in '{s}' with k={k}: {max_length}")
    
    # Merge sorted array
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    tp.merge_sorted_array(nums1, m, nums2, n)
    print(f"Merged sorted array: {nums1}")
    
    # Sort colors
    colors = [2, 0, 2, 1, 1, 0]
    tp.sort_colors(colors)
    print(f"Sorted colors: {colors}") 
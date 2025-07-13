import heapq
from typing import List, Optional, Tuple
from collections import defaultdict


class HeapAlgorithms:
    """
    Comprehensive Heap Algorithms implementation with common patterns and applications.
    
    Heap (Priority Queue) is a specialized tree-based data structure that satisfies
    the heap property. It's particularly useful for problems involving:
    - Finding kth largest/smallest elements
    - Merging sorted arrays
    - Scheduling problems
    - Graph algorithms (Dijkstra, Prim's)
    
    Time Complexity:
    - Insert: O(log n)
    - Extract: O(log n)
    - Peek: O(1)
    - Build: O(n)
    
    Space Complexity: O(n)
    """
    
    def heap_sort(self, arr: List[int]) -> List[int]:
        """
        Sort array using heap sort.
        
        Time Complexity: O(n log n)
        Space Complexity: O(1) in-place
        
        Args:
            arr: Array to sort
            
        Returns:
            Sorted array
        """
        def heapify(arr: List[int], n: int, i: int) -> None:
            """Heapify subtree rooted at index i."""
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        n = len(arr)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        
        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, i, 0)
        
        return arr
    
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        """
        Find kth largest element in array.
        
        Time Complexity: O(n log k)
        Space Complexity: O(k)
        
        Args:
            nums: Input array
            k: kth largest element to find
            
        Returns:
            kth largest element
        """
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
    
    def find_kth_smallest(self, nums: List[int], k: int) -> int:
        """
        Find kth smallest element in array.
        
        Time Complexity: O(n log k)
        Space Complexity: O(k)
        
        Args:
            nums: Input array
            k: kth smallest element to find
            
        Returns:
            kth smallest element
        """
        max_heap = []
        
        for num in nums:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return -max_heap[0]
    
    def merge_k_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        """
        Merge k sorted arrays into one sorted array.
        
        Time Complexity: O(n log k) where n is total elements
        Space Complexity: O(k)
        
        Args:
            arrays: List of sorted arrays
            
        Returns:
            Merged sorted array
        """
        if not arrays:
            return []
        
        result = []
        min_heap = []
        
        # Initialize heap with first element from each array
        for i, arr in enumerate(arrays):
            if arr:
                heapq.heappush(min_heap, (arr[0], i, 0))
        
        while min_heap:
            val, arr_idx, elem_idx = heapq.heappop(min_heap)
            result.append(val)
            
            # Add next element from the same array
            if elem_idx + 1 < len(arrays[arr_idx]):
                heapq.heappush(min_heap, (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))
        
        return result
    
    def top_k_frequent_elements(self, nums: List[int], k: int) -> List[int]:
        """
        Find top k frequent elements.
        
        Time Complexity: O(n log k)
        Space Complexity: O(n)
        
        Args:
            nums: Input array
            k: Number of most frequent elements
            
        Returns:
            List of top k frequent elements
        """
        # Count frequencies
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # Use min heap to keep top k frequent elements
        min_heap = []
        for num, count in freq.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for count, num in min_heap]
    
    def top_k_frequent_words(self, words: List[str], k: int) -> List[str]:
        """
        Find top k frequent words.
        
        Time Complexity: O(n log k)
        Space Complexity: O(n)
        
        Args:
            words: List of words
            k: Number of most frequent words
            
        Returns:
            List of top k frequent words
        """
        # Count frequencies
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        
        # Use min heap with negative count for max heap behavior
        min_heap = []
        for word, count in freq.items():
            heapq.heappush(min_heap, (count, word))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Sort by frequency (descending) and then lexicographically
        result = [(count, word) for count, word in min_heap]
        result.sort(key=lambda x: (-x[0], x[1]))
        
        return [word for count, word in result]
    
    def median_finder(self) -> 'MedianFinder':
        """
        Create a median finder that can find median of data stream.
        
        Returns:
            MedianFinder instance
        """
        return MedianFinder()
    
    def sliding_window_median(self, nums: List[int], k: int) -> List[float]:
        """
        Find median for each sliding window of size k.
        
        Time Complexity: O(n log k)
        Space Complexity: O(k)
        
        Args:
            nums: Input array
            k: Window size
            
        Returns:
            List of medians for each window
        """
        if not nums or k == 0:
            return []
        
        result = []
        max_heap = []  # Left half (smaller elements)
        min_heap = []  # Right half (larger elements)
        
        for i in range(len(nums)):
            # Add new element
            if not max_heap or nums[i] <= -max_heap[0]:
                heapq.heappush(max_heap, -nums[i])
            else:
                heapq.heappush(min_heap, nums[i])
            
            # Balance heaps
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            
            # Remove element outside window
            if i >= k:
                element_to_remove = nums[i - k]
                if element_to_remove <= -max_heap[0]:
                    max_heap.remove(-element_to_remove)
                    heapq.heapify(max_heap)
                else:
                    min_heap.remove(element_to_remove)
                    heapq.heapify(min_heap)
                
                # Rebalance after removal
                if len(max_heap) > len(min_heap) + 1:
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))
                elif len(min_heap) > len(max_heap):
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))
            
            # Calculate median
            if i >= k - 1:
                if len(max_heap) == len(min_heap):
                    median = (-max_heap[0] + min_heap[0]) / 2
                else:
                    median = -max_heap[0]
                result.append(median)
        
        return result
    
    def k_closest_points_to_origin(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Find k closest points to origin.
        
        Time Complexity: O(n log k)
        Space Complexity: O(k)
        
        Args:
            points: List of [x, y] coordinates
            k: Number of closest points
            
        Returns:
            List of k closest points
        """
        max_heap = []
        
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(max_heap, (-distance, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [point for distance, point in max_heap]
    
    def connect_ropes_minimum_cost(self, ropes: List[int]) -> int:
        """
        Connect ropes with minimum cost.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Args:
            ropes: List of rope lengths
            
        Returns:
            Minimum cost to connect all ropes
        """
        if len(ropes) <= 1:
            return 0
        
        min_heap = ropes.copy()
        heapq.heapify(min_heap)
        
        total_cost = 0
        
        while len(min_heap) > 1:
            rope1 = heapq.heappop(min_heap)
            rope2 = heapq.heappop(min_heap)
            
            cost = rope1 + rope2
            total_cost += cost
            
            heapq.heappush(min_heap, cost)
        
        return total_cost
    
    def reorganize_string(self, s: str) -> str:
        """
        Reorganize string so no adjacent characters are same.
        
        Time Complexity: O(n log k) where k is unique characters
        Space Complexity: O(n)
        
        Args:
            s: Input string
            
        Returns:
            Reorganized string or empty string if impossible
        """
        # Count character frequencies
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        # Use max heap to get most frequent characters first
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        result = []
        prev_char = None
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            
            if prev_char == char:
                if not max_heap:
                    return ""  # Impossible to reorganize
                
                # Get next character
                next_count, next_char = heapq.heappop(max_heap)
                result.append(next_char)
                
                # Put back characters
                if next_count + 1 < 0:
                    heapq.heappush(max_heap, (next_count + 1, next_char))
                heapq.heappush(max_heap, (count, char))
                
                prev_char = next_char
            else:
                result.append(char)
                if count + 1 < 0:
                    heapq.heappush(max_heap, (count + 1, char))
                prev_char = char
        
        return ''.join(result)
    
    def task_scheduler(self, tasks: List[str], n: int) -> int:
        """
        Find minimum time to complete all tasks with cooldown.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            tasks: List of task types
            n: Cooldown period
            
        Returns:
            Minimum time to complete all tasks
        """
        # Count frequencies
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        # Find maximum frequency
        max_freq = max(freq.values())
        
        # Count tasks with maximum frequency
        max_freq_count = sum(1 for f in freq.values() if f == max_freq)
        
        # Calculate minimum time
        min_time = (max_freq - 1) * (n + 1) + max_freq_count
        
        return max(min_time, len(tasks))
    
    def minimum_cost_to_hire_k_workers(self, quality: List[int], wage: List[int], k: int) -> float:
        """
        Find minimum cost to hire k workers.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Args:
            quality: List of worker qualities
            wage: List of worker wages
            k: Number of workers to hire
            
        Returns:
            Minimum cost
        """
        # Calculate wage/quality ratio for each worker
        workers = [(wage[i] / quality[i], quality[i]) for i in range(len(quality))]
        workers.sort()  # Sort by ratio
        
        min_cost = float('inf')
        quality_sum = 0
        max_heap = []
        
        for ratio, q in workers:
            quality_sum += q
            heapq.heappush(max_heap, -q)
            
            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)
            
            if len(max_heap) == k:
                min_cost = min(min_cost, ratio * quality_sum)
        
        return min_cost


class MedianFinder:
    """
    Median Finder for data stream.
    """
    
    def __init__(self):
        self.max_heap = []  # Left half (smaller elements)
        self.min_heap = []  # Right half (larger elements)
    
    def add_num(self, num: int) -> None:
        """
        Add number to data stream.
        
        Time Complexity: O(log n)
        """
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def find_median(self) -> float:
        """
        Find median of data stream.
        
        Time Complexity: O(1)
        """
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]


# Example usage and testing
if __name__ == "__main__":
    print("Heap Algorithms Demo:")
    print("====================")
    
    ha = HeapAlgorithms()
    
    # Heap Sort
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = ha.heap_sort(arr.copy())
    print(f"Heap sort: {arr} -> {sorted_arr}")
    
    # Find Kth Largest
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    kth_largest = ha.find_kth_largest(nums, k)
    print(f"{k}th largest in {nums}: {kth_largest}")
    
    # Find Kth Smallest
    kth_smallest = ha.find_kth_smallest(nums, k)
    print(f"{k}th smallest in {nums}: {kth_smallest}")
    
    # Merge K Sorted Arrays
    arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged = ha.merge_k_sorted_arrays(arrays)
    print(f"Merged {arrays}: {merged}")
    
    # Top K Frequent Elements
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    top_k = ha.top_k_frequent_elements(nums, k)
    print(f"Top {k} frequent elements in {nums}: {top_k}")
    
    # Top K Frequent Words
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    top_words = ha.top_k_frequent_words(words, k)
    print(f"Top {k} frequent words: {top_words}")
    
    # Median Finder
    mf = ha.median_finder()
    for num in [1, 2, 3, 4, 5]:
        mf.add_num(num)
        print(f"Median after adding {num}: {mf.find_median()}")
    
    # Sliding Window Median
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    medians = ha.sliding_window_median(nums, k)
    print(f"Sliding window medians for {nums} with k={k}: {medians}")
    
    # K Closest Points
    points = [[1, 3], [-2, 2]]
    k = 1
    closest = ha.k_closest_points_to_origin(points, k)
    print(f"{k} closest points to origin: {closest}")
    
    # Connect Ropes
    ropes = [4, 2, 7, 6, 9]
    min_cost = ha.connect_ropes_minimum_cost(ropes)
    print(f"Minimum cost to connect ropes {ropes}: {min_cost}")
    
    # Reorganize String
    s = "aab"
    reorganized = ha.reorganize_string(s)
    print(f"Reorganized '{s}': '{reorganized}'")
    
    # Task Scheduler
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    min_time = ha.task_scheduler(tasks, n)
    print(f"Minimum time for tasks {tasks} with cooldown {n}: {min_time}")
    
    # Performance comparison
    print("\n" + "="*50)
    print("Performance Comparison:")
    print("="*50)
    
    import time
    
    # Test with large array
    n = 10000
    large_arr = list(range(n, 0, -1))
    
    start = time.time()
    sorted_large = ha.heap_sort(large_arr.copy())
    heap_sort_time = time.time() - start
    
    start = time.time()
    sorted_large_builtin = sorted(large_arr)
    builtin_sort_time = time.time() - start
    
    print(f"Heap sort time: {heap_sort_time:.4f}s")
    print(f"Built-in sort time: {builtin_sort_time:.4f}s")
    print(f"Speedup: {heap_sort_time/builtin_sort_time:.2f}x") 
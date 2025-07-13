from typing import List, Optional


class BinaryIndexedTree:
    """
    Binary Indexed Tree (Fenwick Tree) implementation.
    
    A Binary Indexed Tree is a data structure that provides efficient methods for:
    - Calculating prefix sums
    - Updating individual elements
    - Range sum queries
    
    Key Features:
    - O(log n) time complexity for both updates and queries
    - O(n) space complexity
    - Efficient for dynamic prefix sum problems
    
    Applications:
    - Range sum queries with updates
    - Inversion counting
    - Order statistics
    - 2D range queries
    """
    
    def __init__(self, size: int):
        """
        Initialize Binary Indexed Tree with given size.
        
        Args:
            size: Number of elements (1-indexed)
        """
        self.size = size
        self.tree = [0] * (size + 1)  # 1-indexed
    
    def update(self, index: int, delta: int) -> None:
        """
        Update element at index by adding delta.
        
        Time Complexity: O(log n)
        
        Args:
            index: 1-indexed position to update
            delta: Value to add
        """
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index  # Add least significant bit
    
    def query(self, index: int) -> int:
        """
        Get prefix sum from 1 to index (inclusive).
        
        Time Complexity: O(log n)
        
        Args:
            index: 1-indexed position
            
        Returns:
            Prefix sum from 1 to index
        """
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index  # Remove least significant bit
        return result
    
    def range_query(self, left: int, right: int) -> int:
        """
        Get sum of range [left, right] (inclusive).
        
        Time Complexity: O(log n)
        
        Args:
            left: Left boundary (1-indexed)
            right: Right boundary (1-indexed)
            
        Returns:
            Sum of range [left, right]
        """
        return self.query(right) - self.query(left - 1)
    
    def get_value(self, index: int) -> int:
        """
        Get value at specific index.
        
        Time Complexity: O(log n)
        
        Args:
            index: 1-indexed position
            
        Returns:
            Value at index
        """
        return self.range_query(index, index)
    
    def set_value(self, index: int, value: int) -> None:
        """
        Set value at specific index.
        
        Time Complexity: O(log n)
        
        Args:
            index: 1-indexed position
            value: New value
        """
        current_value = self.get_value(index)
        self.update(index, value - current_value)
    
    def build_from_array(self, arr: List[int]) -> None:
        """
        Build BIT from array.
        
        Time Complexity: O(n log n)
        
        Args:
            arr: Input array (0-indexed)
        """
        for i, val in enumerate(arr):
            self.update(i + 1, val)
    
    def get_array(self) -> List[int]:
        """
        Get current array representation.
        
        Time Complexity: O(n log n)
        
        Returns:
            Array representation
        """
        return [self.get_value(i) for i in range(1, self.size + 1)]


class BinaryIndexedTree2D:
    """
    2D Binary Indexed Tree for 2D range queries and updates.
    
    Supports:
    - Point updates
    - Range sum queries
    - 2D prefix sums
    """
    
    def __init__(self, rows: int, cols: int):
        """
        Initialize 2D BIT.
        
        Args:
            rows: Number of rows
            cols: Number of columns
        """
        self.rows = rows
        self.cols = cols
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    def update(self, row: int, col: int, delta: int) -> None:
        """
        Update element at (row, col) by adding delta.
        
        Time Complexity: O(log rows * log cols)
        
        Args:
            row: Row index (1-indexed)
            col: Column index (1-indexed)
            delta: Value to add
        """
        i = row
        while i <= self.rows:
            j = col
            while j <= self.cols:
                self.tree[i][j] += delta
                j += j & -j
            i += i & -i
    
    def query(self, row: int, col: int) -> int:
        """
        Get prefix sum from (1,1) to (row, col).
        
        Time Complexity: O(log rows * log cols)
        
        Args:
            row: Row index (1-indexed)
            col: Column index (1-indexed)
            
        Returns:
            Prefix sum
        """
        result = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                result += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return result
    
    def range_query(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Get sum of rectangle from (row1, col1) to (row2, col2).
        
        Time Complexity: O(log rows * log cols)
        
        Args:
            row1, col1: Top-left corner (1-indexed)
            row2, col2: Bottom-right corner (1-indexed)
            
        Returns:
            Sum of rectangle
        """
        return (self.query(row2, col2) - self.query(row2, col1 - 1) - 
                self.query(row1 - 1, col2) + self.query(row1 - 1, col1 - 1))
    
    def build_from_matrix(self, matrix: List[List[int]]) -> None:
        """
        Build 2D BIT from matrix.
        
        Time Complexity: O(rows * cols * log rows * log cols)
        
        Args:
            matrix: Input matrix
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.update(i + 1, j + 1, matrix[i][j])


class BinaryIndexedTreeApplications:
    """
    Common applications and problems solved using Binary Indexed Trees.
    """
    
    @staticmethod
    def count_inversions(arr: List[int]) -> int:
        """
        Count inversions in array using coordinate compression and BIT.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Args:
            arr: Input array
            
        Returns:
            Number of inversions
        """
        # Coordinate compression
        sorted_arr = sorted(set(arr))
        rank = {val: i for i, val in enumerate(sorted_arr)}
        
        # Count inversions
        bit = BinaryIndexedTree(len(sorted_arr))
        inversions = 0
        
        for i in range(len(arr) - 1, -1, -1):
            current_rank = rank[arr[i]]
            inversions += bit.query(current_rank)
            bit.update(current_rank + 1, 1)
        
        return inversions
    
    @staticmethod
    def range_sum_queries_with_updates(arr: List[int], queries: List[List]) -> List[int]:
        """
        Handle range sum queries with updates.
        
        Args:
            arr: Input array
            queries: List of queries
                    [1, index, value] - update arr[index] = value
                    [2, left, right] - sum of range [left, right]
            
        Returns:
            List of query results
        """
        bit = BinaryIndexedTree(len(arr))
        bit.build_from_array(arr)
        
        results = []
        for query in queries:
            if query[0] == 1:  # Update
                index, value = query[1], query[2]
                bit.set_value(index + 1, value)
            else:  # Range query
                left, right = query[1], query[2]
                results.append(bit.range_query(left + 1, right + 1))
        
        return results
    
    @staticmethod
    def kth_smallest_element(arr: List[int], k: int) -> int:
        """
        Find kth smallest element using BIT.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Args:
            arr: Input array
            k: kth smallest element to find (1-indexed)
            
        Returns:
            kth smallest element
        """
        # Coordinate compression
        sorted_arr = sorted(set(arr))
        rank = {val: i for i, val in enumerate(sorted_arr)}
        
        # Build BIT
        bit = BinaryIndexedTree(len(sorted_arr))
        for num in arr:
            bit.update(rank[num] + 1, 1)
        
        # Find kth smallest
        left, right = 1, len(sorted_arr)
        while left < right:
            mid = (left + right) // 2
            if bit.query(mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        return sorted_arr[left - 1]
    
    @staticmethod
    def longest_increasing_subsequence_with_bit(arr: List[int]) -> int:
        """
        Find longest increasing subsequence using BIT.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Args:
            arr: Input array
            
        Returns:
            Length of longest increasing subsequence
        """
        # Coordinate compression
        sorted_arr = sorted(set(arr))
        rank = {val: i for i, val in enumerate(sorted_arr)}
        
        # Find LIS
        bit = BinaryIndexedTree(len(sorted_arr))
        
        for num in arr:
            current_rank = rank[num]
            max_lis = bit.query(current_rank)
            bit.update(current_rank + 1, max_lis + 1 - bit.get_value(current_rank + 1))
        
        return bit.query(len(sorted_arr))
    
    @staticmethod
    def range_minimum_queries_with_updates(arr: List[int], queries: List[List]) -> List[int]:
        """
        Handle range minimum queries with updates using BIT.
        Note: This is a simplified version. For efficient RMQ, use Segment Tree.
        
        Args:
            arr: Input array
            queries: List of queries
                    [1, index, value] - update arr[index] = value
                    [2, left, right] - minimum of range [left, right]
            
        Returns:
            List of query results
        """
        # For RMQ, we need to maintain a different structure
        # This is a simplified implementation
        results = []
        current_arr = arr.copy()
        
        for query in queries:
            if query[0] == 1:  # Update
                index, value = query[1], query[2]
                current_arr[index] = value
            else:  # Range minimum query
                left, right = query[1], query[2]
                results.append(min(current_arr[left:right + 1]))
        
        return results


# Example usage and testing
if __name__ == "__main__":
    print("Binary Indexed Tree Demo:")
    print("========================")
    
    # Basic BIT operations
    arr = [1, 3, 5, 7, 9, 11]
    print(f"Original array: {arr}")
    
    bit = BinaryIndexedTree(len(arr))
    bit.build_from_array(arr)
    
    # Prefix sum queries
    print(f"Prefix sum [1, 3]: {bit.range_query(1, 3)}")
    print(f"Prefix sum [1, 6]: {bit.range_query(1, 6)}")
    print(f"Prefix sum [2, 4]: {bit.range_query(2, 4)}")
    
    # Update operations
    bit.update(3, 5)  # Add 5 to index 3
    print(f"After adding 5 to index 3: {bit.get_array()}")
    print(f"Prefix sum [1, 3] after update: {bit.range_query(1, 3)}")
    
    # Set value
    bit.set_value(2, 10)
    print(f"After setting index 2 to 10: {bit.get_array()}")
    
    # 2D BIT
    print("\n" + "="*50)
    print("2D Binary Indexed Tree Demo:")
    print("="*50)
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original matrix:")
    for row in matrix:
        print(f"  {row}")
    
    bit2d = BinaryIndexedTree2D(3, 3)
    bit2d.build_from_matrix(matrix)
    
    # 2D range queries
    print(f"Sum of rectangle [1,1] to [2,2]: {bit2d.range_query(1, 1, 2, 2)}")
    print(f"Sum of rectangle [1,1] to [3,3]: {bit2d.range_query(1, 1, 3, 3)}")
    
    # Update 2D
    bit2d.update(2, 2, 5)
    print(f"Sum of rectangle [1,1] to [2,2] after update: {bit2d.range_query(1, 1, 2, 2)}")
    
    # Applications
    print("\n" + "="*50)
    print("Binary Indexed Tree Applications:")
    print("="*50)
    
    # Count inversions
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    inversions = BinaryIndexedTreeApplications.count_inversions(arr)
    print(f"Number of inversions in {arr}: {inversions}")
    
    # Range sum queries with updates
    arr = [1, 2, 3, 4, 5]
    queries = [
        [2, 1, 3],  # Sum of range [1, 3]
        [1, 2, 10], # Update arr[2] = 10
        [2, 1, 3],  # Sum of range [1, 3] after update
    ]
    
    results = BinaryIndexedTreeApplications.range_sum_queries_with_updates(arr, queries)
    print(f"Range sum query results: {results}")
    
    # Kth smallest element
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    k = 4
    kth_smallest = BinaryIndexedTreeApplications.kth_smallest_element(arr, k)
    print(f"{k}th smallest element in {arr}: {kth_smallest}")
    
    # Longest Increasing Subsequence
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    lis_length = BinaryIndexedTreeApplications.longest_increasing_subsequence_with_bit(arr)
    print(f"Length of LIS in {arr}: {lis_length}")
    
    # Performance comparison
    print("\n" + "="*50)
    print("Performance Comparison:")
    print("="*50)
    
    import time
    
    # Test with large array
    n = 10000
    large_arr = list(range(n))
    
    # Time BIT operations
    start = time.time()
    bit = BinaryIndexedTree(n)
    bit.build_from_array(large_arr)
    for i in range(1000):
        bit.range_query(1, min(i + 100, n))
    bit_time = time.time() - start
    
    # Time naive approach
    start = time.time()
    for i in range(1000):
        left, right = 0, min(i + 100, n - 1)
        sum(large_arr[left:right + 1])
    naive_time = time.time() - start
    
    print(f"BIT time: {bit_time:.4f}s")
    print(f"Naive approach time: {naive_time:.4f}s")
    print(f"Speedup: {naive_time/bit_time:.2f}x")
    
    # Memory usage comparison
    print(f"BIT memory: O({n})")
    print(f"Naive approach memory: O(1) for queries, O(n) for updates") 
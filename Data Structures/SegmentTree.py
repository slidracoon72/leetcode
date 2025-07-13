from typing import List, Callable, Optional
import math


class SegmentTree:
    """
    Segment Tree implementation for range queries and updates.
    
    A Segment Tree is a data structure that allows efficient range queries and updates.
    It's particularly useful for problems involving:
    - Range sum queries
    - Range minimum/maximum queries
    - Range updates
    - Dynamic programming with range operations
    
    Time Complexity:
    - Build: O(n)
    - Query: O(log n)
    - Update: O(log n)
    - Range Update: O(log n)
    
    Space Complexity: O(n)
    """
    
    def __init__(self, arr: List[int], operation: Callable = min, default_value: int = float('inf')):
        """
        Initialize Segment Tree with given array and operation.
        
        Args:
            arr: Input array
            operation: Binary operation (min, max, sum, etc.)
            default_value: Default value for empty ranges
        """
        self.n = len(arr)
        self.operation = operation
        self.default_value = default_value
        
        # Calculate size of segment tree
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        
        # Initialize segment tree
        self.tree = [default_value] * (2 * self.size)
        
        # Build the tree
        self._build(arr)
    
    def _build(self, arr: List[int]) -> None:
        """Build the segment tree from the input array."""
        # Fill leaves
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        
        # Build internal nodes
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.operation(self.tree[2 * i], self.tree[2 * i + 1])
    
    def query(self, left: int, right: int) -> int:
        """
        Query range [left, right] (0-indexed, inclusive).
        
        Args:
            left: Left boundary of range
            right: Right boundary of range
            
        Returns:
            Result of operation over the range
        """
        left += self.size
        right += self.size
        result = self.default_value
        
        while left <= right:
            if left % 2 == 1:
                result = self.operation(result, self.tree[left])
                left += 1
            if right % 2 == 0:
                result = self.operation(result, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        
        return result
    
    def update(self, index: int, value: int) -> None:
        """
        Update value at given index.
        
        Args:
            index: Index to update (0-indexed)
            value: New value
        """
        index += self.size
        self.tree[index] = value
        
        # Update parent nodes
        index //= 2
        while index >= 1:
            self.tree[index] = self.operation(self.tree[2 * index], self.tree[2 * index + 1])
            index //= 2
    
    def range_update(self, left: int, right: int, value: int) -> None:
        """
        Update all values in range [left, right] to given value.
        
        Args:
            left: Left boundary of range
            right: Right boundary of range
            value: New value for all elements in range
        """
        left += self.size
        right += self.size
        
        while left <= right:
            if left % 2 == 1:
                self.tree[left] = value
                left += 1
            if right % 2 == 0:
                self.tree[right] = value
                right -= 1
            left //= 2
            right //= 2
    
    def get_array(self) -> List[int]:
        """Get the current array representation."""
        return self.tree[self.size:self.size + self.n]


class LazySegmentTree:
    """
    Lazy Segment Tree for efficient range updates and queries.
    
    This implementation supports lazy propagation for range updates,
    making range operations more efficient.
    """
    
    def __init__(self, arr: List[int], operation: Callable = min, default_value: int = float('inf')):
        """
        Initialize Lazy Segment Tree.
        
        Args:
            arr: Input array
            operation: Binary operation
            default_value: Default value for empty ranges
        """
        self.n = len(arr)
        self.operation = operation
        self.default_value = default_value
        
        # Calculate size
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        
        # Initialize trees
        self.tree = [default_value] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        
        # Build tree
        self._build(arr)
    
    def _build(self, arr: List[int]) -> None:
        """Build the segment tree."""
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.operation(self.tree[2 * i], self.tree[2 * i + 1])
    
    def _push(self, node: int, left: int, right: int) -> None:
        """Push lazy updates to children."""
        if self.lazy[node] != 0:
            # Apply lazy update
            self.tree[node] += self.lazy[node]
            
            if left != right:
                # Propagate to children
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            
            self.lazy[node] = 0
    
    def range_update(self, left: int, right: int, value: int) -> None:
        """
        Add value to all elements in range [left, right].
        
        Args:
            left: Left boundary
            right: Right boundary
            value: Value to add
        """
        self._range_update(1, 0, self.size - 1, left, right, value)
    
    def _range_update(self, node: int, node_left: int, node_right: int, 
                     left: int, right: int, value: int) -> None:
        """Internal range update with lazy propagation."""
        self._push(node, node_left, node_right)
        
        if left > node_right or right < node_left:
            return
        
        if left <= node_left and node_right <= right:
            self.lazy[node] += value
            self._push(node, node_left, node_right)
            return
        
        mid = (node_left + node_right) // 2
        self._range_update(2 * node, node_left, mid, left, right, value)
        self._range_update(2 * node + 1, mid + 1, node_right, left, right, value)
        
        self.tree[node] = self.operation(self.tree[2 * node], self.tree[2 * node + 1])
    
    def query(self, left: int, right: int) -> int:
        """
        Query range [left, right].
        
        Args:
            left: Left boundary
            right: Right boundary
            
        Returns:
            Result of operation over range
        """
        return self._query(1, 0, self.size - 1, left, right)
    
    def _query(self, node: int, node_left: int, node_right: int, 
               left: int, right: int) -> int:
        """Internal query with lazy propagation."""
        self._push(node, node_left, node_right)
        
        if left > node_right or right < node_left:
            return self.default_value
        
        if left <= node_left and node_right <= right:
            return self.tree[node]
        
        mid = (node_left + node_right) // 2
        left_result = self._query(2 * node, node_left, mid, left, right)
        right_result = self._query(2 * node + 1, mid + 1, node_right, left, right)
        
        return self.operation(left_result, right_result)


class SegmentTreeApplications:
    """
    Common applications and problems solved using Segment Trees.
    """
    
    @staticmethod
    def range_sum_queries(arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        Range Sum Queries with updates.
        
        Args:
            arr: Input array
            queries: List of queries [type, left, right, value]
                    type 1: update arr[left] = value
                    type 2: sum of range [left, right]
            
        Returns:
            List of sum query results
        """
        st = SegmentTree(arr, operation=lambda x, y: x + y, default_value=0)
        results = []
        
        for query in queries:
            if query[0] == 1:  # Update
                index, value = query[1], query[3]
                st.update(index, value)
            else:  # Sum query
                left, right = query[1], query[2]
                results.append(st.query(left, right))
        
        return results
    
    @staticmethod
    def range_minimum_queries(arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        Range Minimum Queries.
        
        Args:
            arr: Input array
            queries: List of range queries [left, right]
            
        Returns:
            List of minimum values for each range
        """
        st = SegmentTree(arr, operation=min, default_value=float('inf'))
        results = []
        
        for left, right in queries:
            results.append(st.query(left, right))
        
        return results
    
    @staticmethod
    def range_maximum_queries(arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        Range Maximum Queries.
        
        Args:
            arr: Input array
            queries: List of range queries [left, right]
            
        Returns:
            List of maximum values for each range
        """
        st = SegmentTree(arr, operation=max, default_value=float('-inf'))
        results = []
        
        for left, right in queries:
            results.append(st.query(left, right))
        
        return results
    
    @staticmethod
    def count_inversions(arr: List[int]) -> int:
        """
        Count inversions in array using coordinate compression and segment tree.
        
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
        st = SegmentTree([0] * len(sorted_arr), operation=lambda x, y: x + y, default_value=0)
        inversions = 0
        
        for i in range(len(arr) - 1, -1, -1):
            current_rank = rank[arr[i]]
            inversions += st.query(0, current_rank - 1)
            st.update(current_rank, st.tree[st.size + current_rank] + 1)
        
        return inversions
    
    @staticmethod
    def longest_increasing_subsequence_with_segment_tree(arr: List[int]) -> int:
        """
        Find longest increasing subsequence using segment tree.
        
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
        st = SegmentTree([0] * len(sorted_arr), operation=max, default_value=0)
        
        for num in arr:
            current_rank = rank[num]
            max_lis = st.query(0, current_rank - 1)
            st.update(current_rank, max_lis + 1)
        
        return st.query(0, len(sorted_arr) - 1)


# Example usage and testing
if __name__ == "__main__":
    print("Segment Tree Demo:")
    print("==================")
    
    # Basic Segment Tree operations
    arr = [1, 3, 5, 7, 9, 11]
    print(f"Original array: {arr}")
    
    # Range Sum Queries
    st_sum = SegmentTree(arr, operation=lambda x, y: x + y, default_value=0)
    print(f"Sum of range [1, 3]: {st_sum.query(1, 3)}")
    print(f"Sum of range [0, 5]: {st_sum.query(0, 5)}")
    
    # Update operation
    st_sum.update(2, 10)
    print(f"After updating index 2 to 10: {st_sum.get_array()}")
    print(f"Sum of range [1, 3] after update: {st_sum.query(1, 3)}")
    
    # Range Minimum Queries
    st_min = SegmentTree(arr, operation=min, default_value=float('inf'))
    print(f"Minimum in range [1, 4]: {st_min.query(1, 4)}")
    print(f"Minimum in range [0, 2]: {st_min.query(0, 2)}")
    
    # Range Maximum Queries
    st_max = SegmentTree(arr, operation=max, default_value=float('-inf'))
    print(f"Maximum in range [1, 4]: {st_max.query(1, 4)}")
    print(f"Maximum in range [0, 2]: {st_max.query(0, 2)}")
    
    # Lazy Segment Tree
    print("\n" + "="*50)
    print("Lazy Segment Tree Demo:")
    print("="*50)
    
    lazy_st = LazySegmentTree(arr, operation=lambda x, y: x + y, default_value=0)
    print(f"Original array: {arr}")
    
    # Range update
    lazy_st.range_update(1, 3, 5)
    print(f"After adding 5 to range [1, 3]: {lazy_st.get_array()}")
    
    # Query after range update
    print(f"Sum of range [0, 4] after range update: {lazy_st.query(0, 4)}")
    
    # Applications
    print("\n" + "="*50)
    print("Segment Tree Applications:")
    print("="*50)
    
    # Range Sum Queries with updates
    arr = [1, 2, 3, 4, 5]
    queries = [
        [2, 1, 3, 0],  # Sum of range [1, 3]
        [1, 2, 0, 10], # Update arr[2] = 10
        [2, 1, 3, 0],  # Sum of range [1, 3] after update
    ]
    
    results = SegmentTreeApplications.range_sum_queries(arr, queries)
    print(f"Range sum query results: {results}")
    
    # Count inversions
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    inversions = SegmentTreeApplications.count_inversions(arr)
    print(f"Number of inversions in {arr}: {inversions}")
    
    # Longest Increasing Subsequence
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    lis_length = SegmentTreeApplications.longest_increasing_subsequence_with_segment_tree(arr)
    print(f"Length of LIS in {arr}: {lis_length}")
    
    # Performance comparison
    print("\n" + "="*50)
    print("Performance Comparison:")
    print("="*50)
    
    import time
    
    # Test with large array
    n = 10000
    large_arr = list(range(n))
    
    # Time segment tree build and queries
    start = time.time()
    st = SegmentTree(large_arr, operation=lambda x, y: x + y, default_value=0)
    for i in range(1000):
        st.query(i % n, min(i % n + 100, n - 1))
    build_query_time = time.time() - start
    
    # Time naive approach
    start = time.time()
    for i in range(1000):
        left, right = i % n, min(i % n + 100, n - 1)
        sum(large_arr[left:right + 1])
    naive_time = time.time() - start
    
    print(f"Segment Tree time: {build_query_time:.4f}s")
    print(f"Naive approach time: {naive_time:.4f}s")
    print(f"Speedup: {naive_time/build_query_time:.2f}x") 
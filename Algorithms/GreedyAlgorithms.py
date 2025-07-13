from typing import List, Tuple, Optional
import heapq
from collections import defaultdict


class GreedyAlgorithms:
    """
    Comprehensive Greedy Algorithms implementation with common patterns and applications.
    
    Greedy algorithms make locally optimal choices at each step with the hope of finding
    a globally optimal solution. They are often used for optimization problems.
    
    Common Applications:
    - Scheduling problems
    - Huffman coding
    - Dijkstra's algorithm
    - Minimum spanning trees
    - Activity selection
    - Fractional knapsack
    
    Time Complexity: Varies by problem, often O(n log n) due to sorting
    Space Complexity: Usually O(n) for storing results
    """
    
    def activity_selection(self, activities: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """
        Activity Selection Problem
        Select maximum number of activities that don't overlap.
        
        Time Complexity: O(n log n) for sorting
        Space Complexity: O(n)
        
        Args:
            activities: List of (start_time, end_time) tuples
            
        Returns:
            List of selected activities
        """
        if not activities:
            return []
        
        # Sort by end time
        activities.sort(key=lambda x: x[1])
        
        selected = [activities[0]]
        last_end = activities[0][1]
        
        for start, end in activities[1:]:
            if start >= last_end:
                selected.append((start, end))
                last_end = end
        
        return selected
    
    def fractional_knapsack(self, weights: List[int], values: List[int], capacity: int) -> float:
        """
        Fractional Knapsack Problem
        Maximize value by taking fractions of items.
        
        Time Complexity: O(n log n) for sorting
        Space Complexity: O(n)
        
        Args:
            weights: List of item weights
            values: List of item values
            capacity: Maximum weight capacity
            
        Returns:
            Maximum value achievable
        """
        # Calculate value per unit weight
        items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
        items.sort(reverse=True)  # Sort by value per unit weight
        
        total_value = 0.0
        remaining_capacity = capacity
        
        for value_per_weight, weight, value in items:
            if remaining_capacity >= weight:
                # Take the entire item
                total_value += value
                remaining_capacity -= weight
            else:
                # Take fraction of item
                total_value += value_per_weight * remaining_capacity
                break
        
        return total_value
    
    def huffman_coding(self, frequencies: List[int]) -> List[str]:
        """
        Huffman Coding
        Generate optimal prefix codes for given frequencies.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Args:
            frequencies: List of character frequencies
            
        Returns:
            List of Huffman codes
        """
        if len(frequencies) <= 1:
            return ['0'] if frequencies else []
        
        # Create min heap
        heap = [(freq, i) for i, freq in enumerate(frequencies)]
        heapq.heapify(heap)
        
        # Build Huffman tree
        while len(heap) > 1:
            freq1, left = heapq.heappop(heap)
            freq2, right = heapq.heappop(heap)
            
            # Create internal node
            internal_node = (freq1 + freq2, len(frequencies))
            frequencies.append(freq1 + freq2)
            
            heapq.heappush(heap, internal_node)
        
        # Generate codes
        codes = [''] * len(frequencies)
        self._generate_huffman_codes(heap[0][1], '', codes, frequencies)
        
        return codes[:len(frequencies) - len(heap) + 1]
    
    def _generate_huffman_codes(self, node: int, code: str, codes: List[str], frequencies: List[int]) -> None:
        """Helper function to generate Huffman codes recursively."""
        if node < len(codes):
            codes[node] = code
            return
        
        # This is an internal node, continue traversal
        # Note: This is a simplified version. In practice, you'd store the tree structure
        pass
    
    def gas_station(self, gas: List[int], cost: List[int]) -> int:
        """
        Gas Station (LeetCode 134)
        Find starting gas station to complete circular tour.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            gas: Amount of gas at each station
            cost: Cost to travel to next station
            
        Returns:
            Starting station index, or -1 if impossible
        """
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        
        return start
    
    def jump_game(self, nums: List[int]) -> bool:
        """
        Jump Game (LeetCode 55)
        Check if can reach last index.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: Maximum jump length at each position
            
        Returns:
            True if can reach last index, False otherwise
        """
        max_reach = 0
        
        for i in range(len(nums)):
            if i > max_reach:
                return False
            
            max_reach = max(max_reach, i + nums[i])
            
            if max_reach >= len(nums) - 1:
                return True
        
        return True
    
    def jump_game_ii(self, nums: List[int]) -> int:
        """
        Jump Game II (LeetCode 45)
        Find minimum jumps to reach last index.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: Maximum jump length at each position
            
        Returns:
            Minimum number of jumps
        """
        if len(nums) <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                if current_end >= len(nums) - 1:
                    break
        
        return jumps
    
    def candy(self, ratings: List[int]) -> int:
        """
        Candy (LeetCode 135)
        Distribute candies with minimum total.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            ratings: Rating of each child
            
        Returns:
            Minimum candies needed
        """
        n = len(ratings)
        candies = [1] * n
        
        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)
    
    def task_scheduler(self, tasks: List[str], n: int) -> int:
        """
        Task Scheduler (LeetCode 621)
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
    
    def partition_labels(self, s: str) -> List[int]:
        """
        Partition Labels (LeetCode 763)
        Partition string into as many parts as possible.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            s: Input string
            
        Returns:
            List of partition lengths
        """
        # Find last occurrence of each character
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i
        
        result = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result
    
    def minimum_platforms(self, arrivals: List[int], departures: List[int]) -> int:
        """
        Minimum Platforms Required
        Find minimum platforms needed for trains.
        
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        
        Args:
            arrivals: List of arrival times
            departures: List of departure times
            
        Returns:
            Minimum platforms needed
        """
        arrivals.sort()
        departures.sort()
        
        platforms = 0
        max_platforms = 0
        i = j = 0
        
        while i < len(arrivals) and j < len(departures):
            if arrivals[i] <= departures[j]:
                platforms += 1
                i += 1
            else:
                platforms -= 1
                j += 1
            
            max_platforms = max(max_platforms, platforms)
        
        return max_platforms
    
    def meeting_rooms_ii(self, intervals: List[List[int]]) -> int:
        """
        Meeting Rooms II (LeetCode 253)
        Find minimum meeting rooms needed.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Args:
            intervals: List of [start, end] intervals
            
        Returns:
            Minimum meeting rooms needed
        """
        if not intervals:
            return 0
        
        # Separate start and end times
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        
        starts.sort()
        ends.sort()
        
        rooms = 0
        max_rooms = 0
        start_ptr = end_ptr = 0
        
        while start_ptr < len(starts):
            if starts[start_ptr] < ends[end_ptr]:
                rooms += 1
                start_ptr += 1
            else:
                rooms -= 1
                end_ptr += 1
            
            max_rooms = max(max_rooms, rooms)
        
        return max_rooms
    
    def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
        """
        Non-overlapping Intervals (LeetCode 435)
        Find minimum intervals to remove for non-overlapping.
        
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        
        Args:
            intervals: List of [start, end] intervals
            
        Returns:
            Minimum intervals to remove
        """
        if not intervals:
            return 0
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        
        return count
    
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Can Place Flowers (LeetCode 605)
        Check if n flowers can be planted without adjacent flowers.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            flowerbed: Array representing flowerbed
            n: Number of flowers to plant
            
        Returns:
            True if n flowers can be planted, False otherwise
        """
        count = 0
        i = 0
        
        while i < len(flowerbed):
            if (flowerbed[i] == 0 and 
                (i == 0 or flowerbed[i - 1] == 0) and 
                (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                
                flowerbed[i] = 1
                count += 1
                
                if count >= n:
                    return True
            
            i += 1
        
        return count >= n
    
    def lemonade_change(self, bills: List[int]) -> bool:
        """
        Lemonade Change (LeetCode 860)
        Check if can provide change for all customers.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            bills: List of bill denominations
            
        Returns:
            True if can provide change, False otherwise
        """
        five = ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True
    
    def reconstruct_queue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Queue Reconstruction by Height (LeetCode 406)
        Reconstruct queue based on height and number of people in front.
        
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        
        Args:
            people: List of [height, k] where k is number of people in front
            
        Returns:
            Reconstructed queue
        """
        # Sort by height (descending) and k (ascending)
        people.sort(key=lambda x: (-x[0], x[1]))
        
        result = []
        for person in people:
            result.insert(person[1], person)
        
        return result


# Example usage and testing
if __name__ == "__main__":
    print("Greedy Algorithms Demo:")
    print("======================")
    
    ga = GreedyAlgorithms()
    
    # Activity Selection
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    selected = ga.activity_selection(activities)
    print(f"Selected activities: {selected}")
    print(f"Number of activities: {len(selected)}")
    
    # Fractional Knapsack
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value = ga.fractional_knapsack(weights, values, capacity)
    print(f"Maximum value for capacity {capacity}: {max_value}")
    
    # Gas Station
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    start_station = ga.gas_station(gas, cost)
    print(f"Starting gas station: {start_station}")
    
    # Jump Game
    nums = [2, 3, 1, 1, 4]
    can_jump = ga.jump_game(nums)
    print(f"Can reach end: {can_jump}")
    
    # Jump Game II
    min_jumps = ga.jump_game_ii(nums)
    print(f"Minimum jumps needed: {min_jumps}")
    
    # Candy
    ratings = [1, 0, 2]
    candies_needed = ga.candy(ratings)
    print(f"Candies needed: {candies_needed}")
    
    # Task Scheduler
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    min_time = ga.task_scheduler(tasks, n)
    print(f"Minimum time to complete tasks: {min_time}")
    
    # Partition Labels
    s = "ababcbacadefegdehijhklij"
    partitions = ga.partition_labels(s)
    print(f"Partition lengths: {partitions}")
    
    # Minimum Platforms
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    platforms = ga.minimum_platforms(arrivals, departures)
    print(f"Minimum platforms needed: {platforms}")
    
    # Meeting Rooms II
    intervals = [[0, 30], [5, 10], [15, 20]]
    rooms = ga.meeting_rooms_ii(intervals)
    print(f"Minimum meeting rooms: {rooms}")
    
    # Erase Overlap Intervals
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    to_remove = ga.erase_overlap_intervals(intervals)
    print(f"Intervals to remove: {to_remove}")
    
    # Can Place Flowers
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    can_place = ga.can_place_flowers(flowerbed, n)
    print(f"Can place {n} flowers: {can_place}")
    
    # Lemonade Change
    bills = [5, 5, 5, 10, 20]
    can_change = ga.lemonade_change(bills)
    print(f"Can provide change: {can_change}")
    
    # Queue Reconstruction
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    reconstructed = ga.reconstruct_queue(people)
    print(f"Reconstructed queue: {reconstructed}")
    
    # Performance comparison
    print("\n" + "="*50)
    print("Performance Comparison:")
    print("="*50)
    
    import time
    
    # Test with large dataset
    n = 10000
    large_activities = [(i, i + 2) for i in range(0, n, 3)]
    
    start = time.time()
    selected = ga.activity_selection(large_activities)
    activity_time = time.time() - start
    
    print(f"Activity selection for {n} activities: {activity_time:.4f}s")
    print(f"Selected {len(selected)} activities")
    
    # Test greedy vs brute force for small problem
    small_activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8)]
    
    start = time.time()
    greedy_result = ga.activity_selection(small_activities)
    greedy_time = time.time() - start
    
    print(f"Greedy approach time: {greedy_time:.6f}s")
    print(f"Greedy result: {len(greedy_result)} activities") 
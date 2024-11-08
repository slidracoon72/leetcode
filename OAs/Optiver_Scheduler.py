from dataclasses import dataclass
from collections import defaultdict, deque
from typing import List, Tuple


@dataclass
class ProcessSchedule:
    start_time: int
    end_time: int


@dataclass
class Dependency:
    pid1: int
    pid2: int


class Scheduler:
    def __init__(self, processes: List[ProcessSchedule], dependencies: List[Dependency]):
        self.processes = processes
        self.dependencies = dependencies
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)
        self.schedule = [(0, 0)] * len(processes)  # To store final (start, end) times

        # Build graph and calculate in-degrees for topological sort
        for dep in dependencies:
            self.graph[dep.pid1 - 1].append(dep.pid2 - 1)  # Adjusting for 0-indexed
            self.in_degree[dep.pid2 - 1] += 1

    def print_schedule(self):
        # Topological sort with a queue for all nodes with in-degree 0
        n = len(self.processes)
        queue = deque([i for i in range(n) if self.in_degree[i] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.graph[node]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check for cycle (if topological sort doesn't include all nodes)
        if len(order) != n:
            print("IMPOSSIBLE")
            return

        # Determine start and end times in topologically sorted order
        for pid in order:
            process = self.processes[pid]
            start = max(process.start_time, max((self.schedule[dep][1] for dep in self.graph[pid]), default=0) + 1)
            end = start + (process.end_time - process.start_time) - 1
            if start > process.end_time or end > process.end_time:
                print("IMPOSSIBLE")
                return
            self.schedule[pid] = (start, end)

        # Print final schedule in ascending order of PID
        for start, end in self.schedule:
            print(start, end)


# Test the scheduler
processes = [
    ProcessSchedule(start_time=100, end_time=2100),
    ProcessSchedule(start_time=110, end_time=2200),
    ProcessSchedule(start_time=200, end_time=2330)
]

dependencies = [
    Dependency(pid1=1, pid2=2),
    Dependency(pid1=3, pid2=2)
]

scheduler = Scheduler(processes, dependencies)
scheduler.print_schedule()

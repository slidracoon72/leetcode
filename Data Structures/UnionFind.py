from typing import Dict, List, Optional


class UnionFind:
    """
    Union-Find (Disjoint Set) data structure with optimizations.
    
    Features:
    - Path compression: Makes future queries faster
    - Union by rank: Keeps the tree balanced
    - Size tracking: Track size of each connected component
    - Count tracking: Track number of connected components
    
    Time Complexity:
    - Union: O(α(n)) amortized where α is the inverse Ackermann function
    - Find: O(α(n)) amortized
    - Connected: O(α(n)) amortized
    
    Space Complexity: O(n) where n is the number of elements
    
    Applications:
    - Kruskal's algorithm for MST
    - Connected components in graphs
    - Network connectivity problems
    - Image processing (connected component labeling)
    """
    
    def __init__(self, size: int):
        """
        Initialize Union-Find with given size.
        
        Args:
            size: Number of elements (0 to size-1)
        """
        self.size = size
        self.parent = list(range(size))  # Each element is its own parent initially
        self.rank = [0] * size           # Rank of each element (height of subtree)
        self.component_size = [1] * size # Size of each connected component
        self.count = size                # Number of connected components
    
    def find(self, x: int) -> int:
        """
        Find the root (representative) of the set containing element x.
        Uses path compression for optimization.
        
        Args:
            x: Element to find
            
        Returns:
            Root of the set containing x
        """
        if self.parent[x] != x:
            # Path compression: make every node point directly to the root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        """
        Union the sets containing elements x and y.
        Uses union by rank for optimization.
        
        Args:
            x: First element
            y: Second element
            
        Returns:
            True if union was performed, False if elements were already in same set
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same set
        
        # Union by rank: attach smaller tree to larger tree
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.component_size[root_x] += self.component_size[root_y]
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        self.count -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        """
        Check if elements x and y are in the same connected component.
        
        Args:
            x: First element
            y: Second element
            
        Returns:
            True if x and y are connected, False otherwise
        """
        return self.find(x) == self.find(y)
    
    def get_component_size(self, x: int) -> int:
        """
        Get the size of the connected component containing element x.
        
        Args:
            x: Element to check
            
        Returns:
            Size of the connected component
        """
        root = self.find(x)
        return self.component_size[root]
    
    def get_count(self) -> int:
        """
        Get the number of connected components.
        
        Returns:
            Number of connected components
        """
        return self.count
    
    def get_components(self) -> Dict[int, List[int]]:
        """
        Get all connected components.
        
        Returns:
            Dictionary mapping root to list of elements in that component
        """
        components = {}
        
        for i in range(self.size):
            root = self.find(i)
            if root not in components:
                components[root] = []
            components[root].append(i)
        
        return components
    
    def is_connected(self) -> bool:
        """
        Check if all elements are connected (single component).
        
        Returns:
            True if all elements are connected, False otherwise
        """
        return self.count == 1
    
    def reset(self) -> None:
        """
        Reset the Union-Find to initial state.
        """
        self.parent = list(range(self.size))
        self.rank = [0] * self.size
        self.component_size = [1] * self.size
        self.count = self.size


class UnionFindWithPathCompression:
    """
    Alternative Union-Find implementation with explicit path compression.
    This version shows the path compression more clearly.
    """
    
    def __init__(self, size: int):
        self.size = size
        self.parent = list(range(size))
        self.rank = [0] * size
        self.count = size
    
    def find(self, x: int) -> int:
        """
        Find with explicit path compression.
        """
        # Find the root
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        
        # Path compression: update all nodes on the path to point to root
        while x != root:
            next_x = self.parent[x]
            self.parent[x] = root
            x = next_x
        
        return root
    
    def union(self, x: int, y: int) -> bool:
        """
        Union with union by rank.
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        self.count -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class UnionFindApplications:
    """
    Common applications and algorithms using Union-Find.
    """
    
    @staticmethod
    def number_of_provinces(is_connected: List[List[int]]) -> int:
        """
        LeetCode 547: Number of Provinces
        Find the number of connected components in a graph.
        
        Time Complexity: O(n^2 * α(n)) where n is number of cities
        Space Complexity: O(n)
        
        Args:
            is_connected: Adjacency matrix representing connections
            
        Returns:
            Number of provinces (connected components)
        """
        n = len(is_connected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i + 1, n):
                if is_connected[i][j] == 1:
                    uf.union(i, j)
        
        return uf.get_count()
    
    @staticmethod
    def redundant_connection(edges: List[List[int]]) -> List[int]:
        """
        LeetCode 684: Redundant Connection
        Find the edge that creates a cycle in an undirected graph.
        
        Time Complexity: O(n * α(n)) where n is number of edges
        Space Complexity: O(n)
        
        Args:
            edges: List of edges [u, v]
            
        Returns:
            The edge that creates a cycle
        """
        # Find the maximum vertex number
        max_vertex = max(max(edge) for edge in edges)
        uf = UnionFind(max_vertex + 1)
        
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge
        
        return []
    
    @staticmethod
    def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
        """
        LeetCode 721: Accounts Merge
        Merge accounts that share common email addresses.
        
        Time Complexity: O(n * m * α(n)) where n is number of accounts, m is emails per account
        Space Complexity: O(n * m)
        
        Args:
            accounts: List of accounts [name, email1, email2, ...]
            
        Returns:
            Merged accounts
        """
        uf = UnionFind(len(accounts))
        email_to_account = {}
        
        # Union accounts that share emails
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i
        
        # Group emails by account
        account_emails = {}
        for email, account_id in email_to_account.items():
            root = uf.find(account_id)
            if root not in account_emails:
                account_emails[root] = set()
            account_emails[root].add(email)
        
        # Build result
        result = []
        for root, emails in account_emails.items():
            name = accounts[root][0]
            result.append([name] + sorted(list(emails)))
        
        return result
    
    @staticmethod
    def regions_cut_by_slashes(grid: List[str]) -> int:
        """
        LeetCode 959: Regions Cut By Slashes
        Count regions in a grid divided by slashes.
        
        Time Complexity: O(n^2 * α(n^2)) where n is grid size
        Space Complexity: O(n^2)
        
        Args:
            grid: Grid with slashes
            
        Returns:
            Number of regions
        """
        n = len(grid)
        # Each cell is divided into 4 triangles: 0=top, 1=right, 2=bottom, 3=left
        uf = UnionFind(4 * n * n)
        
        for i in range(n):
            for j in range(n):
                cell = grid[i][j]
                base = 4 * (i * n + j)
                
                if cell == '/':
                    uf.union(base + 0, base + 3)  # top with left
                    uf.union(base + 1, base + 2)  # right with bottom
                elif cell == '\\':
                    uf.union(base + 0, base + 1)  # top with right
                    uf.union(base + 2, base + 3)  # bottom with left
                else:  # cell == ' '
                    uf.union(base + 0, base + 1)
                    uf.union(base + 1, base + 2)
                    uf.union(base + 2, base + 3)
                
                # Connect with adjacent cells
                if i > 0:  # connect with cell above
                    uf.union(base + 0, base - 4 * n + 2)
                if j > 0:  # connect with cell to the left
                    uf.union(base + 3, base - 4 + 1)
        
        return uf.get_count()


# Example usage and testing
if __name__ == "__main__":
    print("Union-Find Data Structure Demo:")
    print("==============================")
    
    # Basic Union-Find operations
    uf = UnionFind(10)
    
    print(f"Initial components: {uf.get_count()}")
    
    # Union operations
    unions = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8), (0, 3)]
    
    for x, y in unions:
        uf.union(x, y)
        print(f"Union({x}, {y}) -> Components: {uf.get_count()}")
    
    # Connected queries
    queries = [(0, 5), (1, 6), (2, 8), (0, 9)]
    for x, y in queries:
        connected = uf.connected(x, y)
        print(f"Connected({x}, {y}): {connected}")
    
    # Component sizes
    for i in range(10):
        size = uf.get_component_size(i)
        print(f"Component size of {i}: {size}")
    
    # Get all components
    components = uf.get_components()
    print(f"\nAll components: {components}")
    
    # Applications demo
    print("\n" + "="*50)
    print("Union-Find Applications Demo:")
    print("="*50)
    
    # Number of provinces
    is_connected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    provinces = UnionFindApplications.number_of_provinces(is_connected)
    print(f"Number of provinces: {provinces}")
    
    # Redundant connection
    edges = [[1, 2], [1, 3], [2, 3]]
    redundant = UnionFindApplications.redundant_connection(edges)
    print(f"Redundant connection: {redundant}")
    
    # Accounts merge
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"]
    ]
    merged = UnionFindApplications.accounts_merge(accounts)
    print(f"Merged accounts: {merged}")
    
    # Performance comparison
    print("\n" + "="*50)
    print("Performance Comparison:")
    print("="*50)
    
    import time
    
    # Test with large number of operations
    n = 10000
    uf1 = UnionFind(n)
    uf2 = UnionFindWithPathCompression(n)
    
    # Time Union-Find with optimizations
    start = time.time()
    for i in range(n - 1):
        uf1.union(i, i + 1)
    for i in range(n):
        uf1.find(i)
    time1 = time.time() - start
    
    # Time Union-Find with explicit path compression
    start = time.time()
    for i in range(n - 1):
        uf2.union(i, i + 1)
    for i in range(n):
        uf2.find(i)
    time2 = time.time() - start
    
    print(f"Optimized Union-Find time: {time1:.4f}s")
    print(f"Explicit path compression time: {time2:.4f}s")
    print(f"Speedup: {time2/time1:.2f}x") 
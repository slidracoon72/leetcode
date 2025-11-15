# -------------------------------
# Robot Path Finder with Constraints
# -------------------------------

# Define the grid (6x7)
grid = [
    ["start", "q", "t", "2", "5", "1", "3"],
    ["4", "3", "1", "q", "2", "3", "2"],
    ["t", "3", "2", "t", "1", "5", "7"],
    ["2", "4", "3", "1", "4", "t", "t"],
    ["2", "t", "3", "8", "1", "q", "2"],
    ["1", "2", "5", "6", "9", "7", "end"]
]

rows, cols = len(grid), len(grid[0])

# Identify checkpoints and obstacles
# q = checkpoint, t = obstacle
checkpoints = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "q"}
obstacles = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "t"}

# Allowed moves: right, down, diagonal down-right
moves = [(0, 1), (1, 0), (1, 1)]


# DFS to explore all paths
def dfs(r, c, visited_q, path, current_sum):
    cell = grid[r][c]
    # Invalid cell (obstacle or revisiting checkpoint)
    if cell == "t":
        return []
    if (r, c) in checkpoints:
        if (r, c) in visited_q:
            return []  # Can't visit a checkpoint twice
        visited_q = visited_q | {(r, c)}
    elif cell not in ["start", "end", "q", "t"]:
        current_sum += int(cell)

    path = path + [(r, c)]
    if cell == "end":
        if visited_q == checkpoints:  # All checkpoints visited
            return [("valid" if current_sum >= 10 else "invalid", path, current_sum)]
        return []

    results = []
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in obstacles:
            results.extend(dfs(nr, nc, visited_q, path, current_sum))
    return results


# Run DFS from start (0,0)
all_paths = dfs(0, 0, set(), [], 0)

# Separate valid and invalid paths
valid_paths = [p for p in all_paths if p[0] == "valid"]
invalid_paths = [p for p in all_paths if p[0] == "invalid"]

# Print results
print(f"Total Paths Visiting All Checkpoints: {len(all_paths)}")
print(f"Valid Paths (Sum >= 10): {len(valid_paths)}")
print(f"Invalid Paths (Sum < 10): {len(invalid_paths)}\n")

print("=== VALID PATHS ===")
for i, (_, path, total) in enumerate(valid_paths, 1):
    cells = [grid[r][c] for r, c in path]
    print(f"{i}. Sum = {total} | Path = {path} | Cells = {cells}")

print("\n=== INVALID PATHS ===")
for i, (_, path, total) in enumerate(invalid_paths, 1):
    cells = [grid[r][c] for r, c in path]
    print(f"{i}. Sum = {total} | Path = {path} | Cells = {cells}")

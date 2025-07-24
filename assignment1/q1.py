# bfs_dfs_problem1.py

from collections import deque

# Sample grid: 0 - path, 1 - wall
grid = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]

rows, cols = len(grid), len(grid[0])
start = (0, 0)
goal = (3, 3)

def bfs(start, goal):
    queue = deque([([start], start)])
    visited = set()

    while queue:
        path, (x, y) = queue.popleft()
        if (x, y) == goal:
            return path
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0 and (nx,ny) not in visited:
                visited.add((nx, ny))
                queue.append((path + [(nx, ny)], (nx, ny)))
    return None

def dfs(path, x, y, visited):
    if (x, y) == goal:
        return path
    visited.add((x, y))
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0 and (nx,ny) not in visited:
            result = dfs(path + [(nx, ny)], nx, ny, visited)
            if result:
                return result
    return None

print("BFS Path:", bfs(start, goal))
print("DFS Path:", dfs([start], start[0], start[1], set()))


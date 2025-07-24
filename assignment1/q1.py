from collections import deque

start = "WWW_EEE"
goal = "EEE_WWW"

def get_neighbors(state):
    neighbors = []
    state = list(state)
    i = state.index('_')

    # Move left
    if i > 0 and state[i - 1] in 'WE':
        new_state = state[:]
        new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
        neighbors.append(''.join(new_state))

    # Move right
    if i < len(state) - 1 and state[i + 1] in 'WE':
        new_state = state[:]
        new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
        neighbors.append(''.join(new_state))

    # Jump left
    if i > 1 and state[i - 2] in 'WE' and state[i - 1] != '_':
        new_state = state[:]
        new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
        neighbors.append(''.join(new_state))

    # Jump right
    if i < len(state) - 2 and state[i + 2] in 'WE' and state[i + 1] != '_':
        new_state = state[:]
        new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
        neighbors.append(''.join(new_state))

    return neighbors

def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        state = path[-1]

        if state == goal:
            return path

        if state not in visited:
            visited.add(state)
            for neighbor in get_neighbors(state):
                queue.append(path + [neighbor])
    return None

def dfs(start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    state = path[-1]
    if state == goal:
        return path

    visited.add(state)
    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            result = dfs(start, goal, visited.copy(), path + [neighbor])
            if result:
                return result
    return None

print("BFS Solution Path:")
print(bfs(start, goal))
print("\nDFS Solution Path:")
print(dfs(start, goal))


from collections import deque

people = {
    "A": 5,    # Amogh
    "M": 10,   # Ameya
    "G": 20,   # Grandmother
    "P": 25    # Grandfather
}

def is_goal(state):
    return len(state["left"]) == 0

def get_neighbors(state):
    neighbors = []
    side = state["side"]

    if side == "left":
        for i in range(len(state["left"])):
            for j in range(i+1, len(state["left"])):
                p1, p2 = state["left"][i], state["left"][j]
                new_left = state["left"][:]
                new_left.remove(p1)
                new_left.remove(p2)
                new_right = state["right"] + [p1, p2]
                time = state["time"] + max(people[p1], people[p2])
                neighbors.append({
                    "left": new_left,
                    "right": new_right,
                    "side": "right",
                    "time": time,
                    "path": state["path"] + [f"{p1},{p2} ->"]
                })
    else:
        for p in state["right"]:
            new_left = state["left"] + [p]
            new_right = state["right"][:]
            new_right.remove(p)
            time = state["time"] + people[p]
            neighbors.append({
                "left": new_left,
                "right": new_right,
                "side": "left",
                "time": time,
                "path": state["path"] + [f"<- {p}"]
            })

    return neighbors

def bfs():
    start = {
        "left": ["A", "M", "G", "P"],
        "right": [],
        "side": "left",
        "time": 0,
        "path": []
    }

    queue = deque([start])

    while queue:
        state = queue.popleft()

        if is_goal(state) and state["time"] <= 60:
            return state

        for neighbor in get_neighbors(state):
            if neighbor["time"] <= 60:
                queue.append(neighbor)
    return None

result = bfs()
if result:
    print("Path:", " → ".join(result["path"]))
    print("Total Time:", result["time"], "minutes")
else:
    print("No valid solution within 60 minutes.")


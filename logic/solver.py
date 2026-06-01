from collections import deque
from model.state import State

def bfs(cap1, cap2, target):
    start = State(0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state.x == target or state.y == target:
            return path

        next_states = [
            State(cap1, state.y),
            State(state.x, cap2),
            State(0, state.y),
            State(state.x, 0),

            State(
                max(0, state.x - (cap2 - state.y)),
                min(cap2, state.y + state.x)
            ),

            State(
                min(cap1, state.x + state.y),
                max(0, state.y - (cap1 - state.x))
            )
        ]

        for nxt in next_states:
            if nxt not in visited:
                queue.append((nxt, path))

    return None

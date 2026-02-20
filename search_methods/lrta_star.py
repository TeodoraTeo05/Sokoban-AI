from typing import Callable, Dict, List, Optional
from sokoban.map import Map

def lrta_star(initial_state: Map,
              heuristic: Callable[[Map], int]) -> Optional[List[Map]]:

    h: Dict[str, int] = {}
    current: Map = initial_state.copy()
    current.explored_states = 0
    path: List[Map] = [current.copy()]
    visited_states = set()

    max_iterations = 50000

    for _ in range(max_iterations):
        if current.is_solved():
            path[-1].explored_states = current.explored_states
            return path

        state_str = str(current)
        if state_str not in h:
            h[state_str] = heuristic(current)

        neighbours: List[Map] = current.get_neighbours()

        if not neighbours:
            h[state_str] += 100
            continue

        min_cost = float('inf')
        best_neighbor = None

        for neighbor in neighbours:
            neighbor_str = str(neighbor)
            if neighbor_str not in h:
                h[neighbor_str] = heuristic(neighbor)

            cost = 1 + h[neighbor_str]
            if cost < min_cost:
                min_cost = cost
                best_neighbor = neighbor

        if best_neighbor is None:
            h[state_str] += 100
            continue
        h[state_str] = min_cost
        current.explored_states += 1
        current = best_neighbor
        path.append(current.copy())

    return None

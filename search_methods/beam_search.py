from typing import Callable, List, Optional, Set, Tuple
from sokoban.map import Map

def beam_search(initial_state: Map, 
                heuristic: Callable[[Map], int], 
                beam_width: int = 5) -> Optional[List[Map]]:
    from heapq import heappush

    frontier: List[Tuple[int, Map, List[Map]]] = [(heuristic(initial_state), initial_state.copy(), [initial_state.copy()])]
    visited: Set[str] = {str(initial_state)}

    total_explored_states = 0

    while frontier:
        frontier = sorted(frontier, key=lambda x: x[0])[:beam_width]
        next_frontier: List[Tuple[int, Map, List[Map]]] = []

        for _, current_state, path in frontier:
            if current_state.is_solved():
                current_state.explored_states = total_explored_states
                return path

            for neighbor in current_state.get_neighbours():
                state_str = str(neighbor)
                if state_str not in visited:
                    visited.add(state_str)
                    new_path = path + [neighbor]
                    score = heuristic(neighbor)
                    heappush(next_frontier, (score, neighbor, new_path))
                    total_explored_states += 1
            
        frontier = next_frontier

    return None


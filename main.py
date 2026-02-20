import sys
import os
from sokoban import (
    Box,
    DOWN,
    Map,
    Player
)
from search_methods.solver import BeamSolver, LRTASolver
from search_methods.heuristics import (
    emm_euclidean_heuristic
)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py <algorithm> <input_map.yaml>")
        print("Algorithm must be 'lrta*' or 'beam_search'")
        sys.exit(1)

    algorithm = sys.argv[1].lower()
    input_map_path = sys.argv[2]

    try:
        crt_map = Map.from_yaml("./tests/" + input_map_path + ".yaml")
    except FileNotFoundError:
        print(f"Error: File '{input_map_path}' not found.")
        sys.exit(1)


    print(crt_map)
    print(f"Is solved: {crt_map.is_solved()}")
    print("Neighbours:")
    for neighbour in crt_map.get_neighbours():
        print(neighbour)

    heuristic = emm_euclidean_heuristic

    if algorithm == 'beam_search':
        solver = BeamSolver(crt_map, heuristic, beam_width=13)
    elif algorithm == 'lrta*':
        solver = LRTASolver(crt_map, heuristic)
    else:
        print(f"Unknown algorithm: {algorithm}")
        sys.exit(1)

    result = solver.solve()

    print(f"\nResults for {algorithm.upper()} on map {input_map_path}:")
    if result:
        print(f"Solution found with {len(result)} steps.")
        print(f"Pull moves: {result[-1].undo_moves}")

        save_images = False
        if save_images:
            output_dir = 'output'
            os.makedirs(output_dir, exist_ok=True)

            for idx, state in enumerate(result):
                save_path = os.path.join(output_dir, f"step_{idx:03}.png")
                state.plot_map(save_path=save_path)

            print(f"Saved {len(result)} images in '{output_dir}/'.")

    else:
        print("No solution found.")

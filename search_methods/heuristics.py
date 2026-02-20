from sokoban.map import Map
from typing import Callable
from typing import List, Tuple
import math
from collections import deque

PENALTY = 0.0

def misplaced_boxes_heuristic(state: Map) -> int:
    misplaced = sum((box.x, box.y) not in state.targets for box in state.boxes.values())
    pull_penalty_per_move = PENALTY
    total_cost = misplaced + pull_penalty_per_move * state.undo_moves

    return total_cost


def manhattan_heuristic(state: Map) -> int:
    total_distance = 0
    for box in state.boxes.values():
        min_dist = min(abs(box.x - tx) + abs(box.y - ty) for tx, ty in state.targets)
        total_distance += min_dist
    pull_penalty_per_move = PENALTY
    total_distance += pull_penalty_per_move * state.undo_moves

    return total_distance


def euclidean_heuristic(state: Map) -> int:
    total_distance = 0
    boxes = list(state.boxes.values())
    targets = list(state.targets)

    for box in boxes:
        min_dist = float('inf')
        for target in targets:
            distance = math.sqrt((box.x - target[0])**2 + (box.y - target[1])**2)
            if distance < min_dist:
                min_dist = distance
        total_distance += min_dist

    pull_penalty_per_move = PENALTY
    total_distance += pull_penalty_per_move * state.undo_moves

    return int(total_distance)


def emm_manhattan_heuristic(state: Map) -> int:
    boxes = list(state.boxes.values())
    targets = list(state.targets)

    cost_matrix = []
    for box in boxes:
        row = []
        for target in targets:
            distance = abs(box.x - target[0]) + abs(box.y - target[1])
            row.append(distance)
        cost_matrix.append(row)
    total_cost = 0
    used_targets = set()

    for box_idx, costs in enumerate(cost_matrix):
        min_cost = float('inf')
        chosen_target = None
        for target_idx, cost in enumerate(costs):
            if target_idx not in used_targets and cost < min_cost:
                min_cost = cost
                chosen_target = target_idx
        
        if chosen_target is not None:
            used_targets.add(chosen_target)
            total_cost += min_cost
    pull_penalty_per_move = PENALTY
    total_cost += pull_penalty_per_move * state.undo_moves

    return total_cost


def emm_euclidean_heuristic(state: Map) -> int:
    boxes = list(state.boxes.values())
    targets = list(state.targets)

    cost_matrix = []
    for box in boxes:
        row = []
        for target in targets:
            distance = math.sqrt((box.x - target[0])**2 + (box.y - target[1])**2)
            row.append(distance)
        cost_matrix.append(row)

    total_cost = 0
    used_targets = set()

    for box_idx, costs in enumerate(cost_matrix):
        min_cost = float('inf')
        chosen_target = None
        for target_idx, cost in enumerate(costs):
            if target_idx not in used_targets and cost < min_cost:
                min_cost = cost
                chosen_target = target_idx
        
        if chosen_target is not None:
            used_targets.add(chosen_target)
            total_cost += min_cost

    pull_penalty_per_move = PENALTY
    total_cost += pull_penalty_per_move * state.undo_moves

    return int(total_cost)

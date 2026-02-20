from sokoban.map import Map
from search_methods.beam_search import beam_search
from search_methods.lrta_star import lrta_star



class Solver:
    def __init__(self, map: Map) -> None:
        self.map = map

    def solve(self):
        raise NotImplementedError

class BeamSolver(Solver):
    def __init__(self, map: Map, h_function, beam_width=5):
        super().__init__(map)
        self.beam_width = beam_width
        self.h_function = h_function

    def solve(self):
        return beam_search(self.map, heuristic=self.h_function, beam_width=self.beam_width)


class LRTASolver(Solver):
    def __init__(self, map: Map, h_function):
        super().__init__(map)
        self.h_function = h_function

    def solve(self):
        return lrta_star(self.map, heuristic=self.h_function)
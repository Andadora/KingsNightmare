class Vertex:
    def __init__(self, index, previous, distance, heuristic_distance, path):
        self.index = index
        self.previous = previous
        self.distance = distance
        self.heuristic_distance = heuristic_distance
        self.combined_heuristic = heuristic_distance + distance
        self.path = path

    def __str__(self):
        return 'index: {:5d} distance: {:5d} path: {:s}\n' .format(self.index, self.distance, self.path)

    def __repr__(self):
        return 'index: {:5d} distance: {:5d} path: {:s}\n' .format(self.index, self.distance, self.path)

    def __lt__(self, other):
        if self.combined_heuristic < other.combined_heuristic:
            return True
        else:
            return False

    def __le__(self, other):
        if self.combined_heuristic <= other.combined_heuristic:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.combined_heuristic == other.combined_heuristic:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.combined_heuristic != other.combined_heuristic:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.combined_heuristic > other.combined_heuristic:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.combined_heuristic >= other.combined_heuristic:
            return True
        else:
            return False

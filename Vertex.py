LETTER_INDEXES = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
                  10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
                  20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y'}


class Vertex:
    def __init__(self, index, previous, graph_distance, heuristic_distance, path):
        self.index = index
        self.previous = previous
        self.graph_distance = graph_distance
        self.heuristic_distance = heuristic_distance
        self.distance = heuristic_distance + graph_distance
        self.path = path
        self.considered = -1

    def __str__(self):
        return f'{LETTER_INDEXES[self.index]} f={self.distance}, h={self.heuristic_distance}, g={self.graph_distance}'

    def __repr__(self):
        return f'{LETTER_INDEXES[self.index]} f={self.distance}, h={self.heuristic_distance}, g={self.graph_distance}'

    def __lt__(self, other):
        if self.distance < other.distance or (self.distance == other.distance and self.index < other.index):
            return True
        else:
            return False

    def __eq__(self, other):
        if self.distance == other.distance:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.distance != other.distance:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.distance > other.distance or (self.distance == other.distance and self.index > other.index):
            return True
        else:
            return False

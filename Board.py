from Graph import Graph
INDEXES = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4,
           (1, 0): 5, (1, 1): 6, (1, 2): 7, (1, 3): 8, (1, 4): 9,
           (2, 0): 10, (2, 1): 11, (2, 2): 12, (2, 3): 13, (2, 4): 14,
           (3, 0): 15, (3, 1): 16, (3, 2): 17, (3, 3): 18, (3, 4): 19,
           (4, 0): 20, (4, 1): 21, (4, 2): 22, (4, 3): 23, (4, 4): 24}

COORDINATES = {'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (0, 4),
               'F': (1, 0), 'G': (1, 1), 'H': (1, 2), 'I': (1, 3), 'J': (1, 4),
               'K': (2, 0), 'L': (2, 1), 'M': (2, 2), 'N': (2, 3), 'O': (2, 4),
               'P': (3, 0), 'Q': (3, 1), 'R': (3, 2), 'S': (3, 3), 'T': (3, 4),
               'U': (4, 0), 'V': (4, 1), 'W': (4, 2), 'X': (4, 3), 'Y': (4, 4)}


class Board:
    def __init__(self, rook='A', king='H', knight='W'):
        self.rook = COORDINATES[rook]
        self.king = COORDINATES[king]
        self.knight = COORDINATES[knight]
        if self.rook[0] != self.knight[0] and self.rook[1] != self.knight[1]:
            print(f'king: {king}, rook: {rook}, knight: {knight}')
            self.generate_graph('graph.txt')
            file = open('graph.txt', 'r').read()
            self.graph = Graph(file)
            self.graph.a_star()
        else:
            print('skoczek nie może startować z pola atakowanego przez wieżę')

# generuje plik z grafem w postaci:
# liczba_wierzchołków, wierzchołek_startowy, wierzchołek_celu
# wierzchołek_poczatkowy, wierzchołek_koncowy, waga
    def generate_graph(self, file_name):
        file = open(file_name, 'w')
        file.write(f'25, {INDEXES[self.knight]}, {INDEXES[self.king]}')

        for x in range(5):
            for y in range(5):
                if x != self.rook[0] and y != self.rook[1]:
                    if x > 1 and y > 0:
                        if x - 2 != self.rook[0] and y - 1 != self.rook[1]:
                            file.write(f'\n{INDEXES[(x, y)]}, {INDEXES[(x - 2, y - 1)]}, {3}')
                    if x > 1 and y < 4:
                        if x - 2 != self.rook[0] and y + 1 != self.rook[1]:
                            file.write(f'\n{INDEXES[(x, y)]}, {INDEXES[(x - 2, y + 1)]}, {3}')
                    if x > 0 and y > 1:
                        if x - 1 != self.rook[0] and y - 2 != self.rook[1]:
                            file.write(f'\n{INDEXES[(x, y)]}, {INDEXES[(x - 1, y - 2)]}, {3}')
                    if x < 4 and y > 1:
                        if x + 1 != self.rook[0] and y - 2 != self.rook[1]:
                            file.write(f'\n{INDEXES[(x, y)]}, {INDEXES[(x + 1, y - 2)]}, {3}')
                    if x > 0 and y < 3:
                        if x - 1 != self.rook[0] and y + 2 != self.rook[1]:
                            file.write(f'\n{INDEXES[(x, y)]}, {INDEXES[(x - 1, y + 2)]}, {3}')
                    if x < 4 and y < 3:
                        if x + 1 != self.rook[0] and y + 2 != self.rook[1]:
                            file.write(f'\n{INDEXES[(x, y)]}, {INDEXES[(x + 1, y + 2)]}, {3}')
                    if x < 3 and y > 0:
                        if x + 2 != self.rook[0] and y - 1 != self.rook[1]:
                            file.write(f'\n{INDEXES[(x, y)]}, {INDEXES[(x + 2, y - 1)]}, {3}')
                    if x < 3 and y < 4:
                        if x + 2 != self.rook[0] and y + 1 != self.rook[1]:
                            file.write(f'\n{INDEXES[(x, y)]}, {INDEXES[(x + 2, y + 1)]}, {3}')
        file.close()

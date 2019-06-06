from Graph import Graph
Dict = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4,
        (1, 0): 5, (1, 1): 6, (1, 2): 7, (1, 3): 8, (1, 4): 9,
        (2, 0): 10, (2, 1): 11, (2, 2): 12, (2, 3): 13, (2, 4): 14,
        (3, 0): 15, (3, 1): 16, (3, 2): 17, (3, 3): 18, (3, 4): 19,
        (4, 0): 20, (4, 1): 21, (4, 2): 22, (4, 3): 23, (4, 4): 24}


class Board:
    def __init__(self, rook_position=(0, 0), king_position=(1, 2), knight_position=(4, 2)):
        self.rook = rook_position
        self.king = king_position
        self.knight_start = knight_position

        self.generate_graph('graph.txt')
        file = open('graph.txt', 'r').read()
        self.graph = Graph(file)
        print(self.graph.a_star())

# generuje plik z grafem w postaci:
# liczba_wierzchołków, wierzchołek_startowy, wierzchołek_celu
# wierzchołek_poczatkowy, wierzchołek_koncowy, waga
    def generate_graph(self, file_name):
        file = open(file_name, 'w')
        file.write(f'25, {Dict[self.knight_start]}, {Dict[self.king]}')

        for x in range(5):
            for y in range(5):
                if x != self.rook[0] and y != self.rook[1]:
                    if x > 1 and y > 0:
                        if x - 2 != self.rook[0] and y - 1 != self.rook[1]:
                            file.write(f'\n{Dict[(x, y)]}, {Dict[(x-2,y-1)]}, {3}')
                    if x > 1 and y < 4:
                        if x - 2 != self.rook[0] and y + 1 != self.rook[1]:
                            file.write(f'\n{Dict[(x, y)]}, {Dict[(x-2,y+1)]}, {3}')
                    if x > 0 and y > 1:
                        if x - 1 != self.rook[0] and y - 2 != self.rook[1]:
                            file.write(f'\n{Dict[(x, y)]}, {Dict[(x-1,y-2)]}, {3}')
                    if x < 4 and y > 1:
                        if x + 1 != self.rook[0] and y - 2 != self.rook[1]:
                            file.write(f'\n{Dict[(x, y)]}, {Dict[(x+1,y-2)]}, {3}')
                    if x > 0 and y < 3:
                        if x - 1 != self.rook[0] and y + 2 != self.rook[1]:
                            file.write(f'\n{Dict[(x, y)]}, {Dict[(x-1,y+2)]}, {3}')
                    if x < 4 and y < 3:
                        if x + 1 != self.rook[0] and y + 2 != self.rook[1]:
                            file.write(f'\n{Dict[(x, y)]}, {Dict[(x+1,y+2)]}, {3}')
                    if x < 3 and y > 0:
                        if x + 2 != self.rook[0] and y - 1 != self.rook[1]:
                            file.write(f'\n{Dict[(x, y)]}, {Dict[(x+2,y-1)]}, {3}')
                    if x < 3 and y < 4:
                        if x + 2 != self.rook[0] and y + 1 != self.rook[1]:
                            file.write(f'\n{Dict[(x, y)]}, {Dict[(x+2,y+1)]}, {3}')
        file.close()

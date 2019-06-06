from MyQueue import MyQueue
from Vertex import Vertex
LETTER_INDEXES = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
                  10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
                  20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y'}


class Graph:
    #   wczytuje graf zapisany w pliku tekstowym w formacie:
    #   liczba_wierzchołków, wierzchołek_startowy, wierzchołek_celu
    #   wierzchołek_poczatkowy, wierzchołek_koncowy, waga
    def __init__(self, file):
        lines = file.split('\n')

        parameters = lines[0].split(', ')
        self.vertices = int(parameters[0])          # liczba wierzcholkow
        self.start = int(parameters[1])             # indeks wierzcholka startowego
        self.target = int(parameters[2])            # indeks wierzchołka celu
        self.adjacency_list = []                    # utworzenie pustej listy sąsiedztwa
        for i in range(self.vertices):    # zagnieżdżenie w liście sąsiedztwa pustych list w liczbie wierzchołków grafu
            self.adjacency_list.append([])

        # wczytanie listy sasiedztwa
        for line in lines[1:]:
            edge = line.split(', ')
            edge_object = [int(edge[1]), int(edge[2])]
            self.adjacency_list[int(edge[0])].append(edge_object)

    def __str__(self):
        return f'vertices:\t\t\t{self.vertices}\nstarting vertex:\t{self.start}\ntarget vertex:\t{self.target}'

    def manhattan(self, start, target):
        x_start = int(start / 5)
        y_start = int(start % 5)
        x_target = int(target / 5)
        y_target = int(target % 5)
        return abs(x_start - x_target) + abs(y_start - y_target)

    def a_star(self):
        que = MyQueue()  # kolejka wierzchołków do sprawdzenia
        finished = MyQueue()    # kolejka skończonych
        counter = 0
        added_to_frontier = []
        que.insert(Vertex(index=self.start,
                          previous=-1,
                          graph_distance=0,
                          heuristic_distance=self.manhattan(self.start, self.target),
                          path=''))
        added_to_frontier.append(self.start)

        while not que.is_empty():
            current = que.remove()
            counter += 1
            current.considered = counter
            if current.index != self.target:
                for child in self.adjacency_list[current.index]:
                    if not que.contains(child[0]) and not finished.contains(child[0]):
                        que.insert(Vertex(index=child[0],
                                          previous=current.index,
                                          graph_distance=current.graph_distance + int(child[1]),
                                          heuristic_distance=self.manhattan(child[0], self.target),
                                          path=f'{current.path}{LETTER_INDEXES[current.index]} -> '))
                        added_to_frontier.append(child[0])
                    elif que.contains(child[0]):
                        if current.distance + child[1] < que[child[0]].distance:
                            que.set_distance(child[0], current.distance + child[1])
                            que.set_previous(child[0], current.index)  # aktualizuj poprzednika
                            que.set_path(child[0], f'{current.path}{LETTER_INDEXES[current.index]} -> ')  # aktualizuj sciezke
                finished.insert(current)
            else:
                while not que.is_empty():
                    finished.insert(que.remove())
                for index in added_to_frontier:
                    print(f'{finished[index].considered}, {finished[index]}')
                print(f'najkrótsza znaleziona ścieżka z {LETTER_INDEXES[self.start]} do {LETTER_INDEXES[self.target]}:')
                print(str(current.path) + str(LETTER_INDEXES[self.target]))
                return str(current.path) + str(LETTER_INDEXES[self.target])
        for index in added_to_frontier:
            print(f'{finished[index].considered}, {finished[index]}')
        print('ścieżka nie została odnaleziona')
        return 'brak ścieżki'

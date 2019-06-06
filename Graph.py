from MyQueue import MyQueue
from Vertex import Vertex


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
        que.insert(Vertex(index=self.start,
                          previous=-1,
                          distance=0,
                          heuristic_distance=self.manhattan(self.start, self.target),
                          path=''))

        while not que.is_empty():
            current = que.remove()
            if current.index != self.target:
                for child in self.adjacency_list[current.index]:
                    if not que.contains(child[0]) and not finished.contains(child[0]):
                        que.insert(Vertex(index=child[0],
                                          previous=current.index,
                                          distance=child[1],
                                          heuristic_distance=self.manhattan(child[0], self.target),
                                          path=f'{current.path}{current.index} -> '))
                    else:
                        if current.distance + child[1] < que[child[0]].distance:
                            que.set_distance(child[0], current.distance + child[1])
                            que.set_previous(child[0], current.index)  # aktualizuj poprzednika
                            que.set_path(child[0], f'{current.path}{current.index} -> ')  # aktualizuj sciezke
                finished.insert(current)
            else:
                return current.path

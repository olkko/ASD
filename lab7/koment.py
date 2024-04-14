class GraphAdjList:
    def __init__(self):
        # Inicjalizacja pustego słownika, który będzie reprezentował graf za pomocą listy sąsiedztwa.
        # Przechowuje on pary (klucz, wartość), gdzie klucz to wierzchołek a wartość to lista sąsiadów.
        self.adjList = {}
        
        # Inicjalizacja pustej listy, która będzie przechowywać wierzchołki grafu.
        self.mapVertex = []

    def edges(self):
        # Metoda zwracająca listę krotek, które reprezentują krawędzie grafu.
        result = []

        # Przechodzimy przez każdy wierzchołek grafu wraz z listą jego sąsiadów.
        # Dla każdego sąsiada dodajemy krotkę (klucz wierzchołka, klucz sąsiada) do listy wynikowej.
        for node, neighbours in self.adjList.items():
            result += [(node.key, neighbour.key) for neighbour in neighbours]

        # Zwracamy listę krotek reprezentujących krawędzie grafu.
        return result

    def isEmpty(self):
        # Metoda zwracająca True, jeśli graf nie zawiera wierzchołków (jest pusty), False w przeciwnym przypadku.
        return not bool(self.adjList)

    def insertVertex(self, vertex):
        # Tworzymy nowy wierzchołek z podanego elementu.
        vertex = Node(vertex)

        # Dodajemy wierzchołek do słownika jako klucz, a do wartości przypisujemy pustą listę sąsiadów.
        self.adjList[vertex] = []

        # Dodajemy wierzchołek do listy wierzchołków grafu.
        self.mapVertex.append(vertex)

    def insertEdge(self, vertex1, vertex2, edge):
        # Tworzymy nowe wierzchołki z podanych elementów.
        vertex1 = Node(vertex1)
        vertex2 = Node(vertex2)

        # Sprawdzamy, czy wierzchołki nie są już sąsiadami. 
        if not (vertex1 in self.adjList[vertex2] and vertex2 in self.adjList[vertex1]):
            # Dodajemy wierzchołki do listy sąsiadów każdego z nich.
            self.adjList[vertex1].append(vertex2)
            self.adjList[vertex2].append(vertex1)

    def deleteVertex(self, vertex):
        # Tworzymy wierzchołek z podanego elementu.
        vertex = Node(vertex)

        # Usuwamy wierzchołek z listy sąsiadów każdego wierzchołka, który jest z nim połączony.
        for node in self.adjList:
            if vertex in self.adjList[node]:
                self.adjList[node].remove(vertex)

        # Usuwamy wierzchołek z grafu.
        del self.adjList[vertex]

        # Usuwamy wierzchołek z listy wierzchołków grafu.
        self.mapVertex.remove(vertex)

    def deleteEdge(self, vertex1, vertex2):
        # Tworzymy wierzchołki z podanych elementów









# Konstruktor klasy, inicjalizujący macierz sąsiedztwa, listę wierzchołków oraz wartość początkową krawędzi.
def __init__(self, initialEdgeSpecifier=0):
    self.adjMatrix = []  # macierz sąsiedztwa grafu
    self.mapVertex = []  # lista wierzchołków grafu
    self.initialEdgeSpecifier = initialEdgeSpecifier  # wartość początkowa krawędzi

# Metoda zwracająca listę krotek, które reprezentują krawędzie grafu.
def edges(self):
    result = []
    for node_id, neighbours in enumerate(self.adjMatrix):
        for neighbour_id, neighbour in enumerate(neighbours):
            if neighbour is not self.initialEdgeSpecifier:
                result.append((self.getVertex(node_id).key, self.getVertex(neighbour_id).key))
    return result

# Metoda sprawdzająca, czy graf jest pusty.
def isEmpty(self):
    return not bool(self.adjMatrix)

# Metoda dodająca wierzchołek do grafu.
def insertVertex(self, vertex):
    self.mapVertex.append(Node(vertex))  # dodajemy nowy wierzchołek do listy wierzchołków grafu

    new_order = self.order() + 1  # aktualizujemy liczbę wierzchołków grafu

    for neighbours in self.adjMatrix:
        neighbours.append(self.initialEdgeSpecifier)

    self.adjMatrix.append([self.initialEdgeSpecifier for i in range(new_order)])  # dodajemy nowy wierzchołek do macierzy sąsiedztwa

# Metoda dodająca krawędź między dwoma wierzchołkami grafu.
def insertEdge(self, vertex1, vertex2, edge):
    idx1 = self.getVertexIdx(vertex1)
    idx2 = self.getVertexIdx(vertex2)

    self.adjMatrix[idx1][idx2] = 1  # ustawiamy wartość krawędzi między wierzchołkami na 1
    self.adjMatrix[idx2][idx1] = 1  # ustawiamy wartość krawędzi między wierzchołkami na 1

# Metoda usuwająca wierzchołek z grafu.
def deleteVertex(self, vertex):
    idx = self.getVertexIdx(vertex)

    self.adjMatrix.pop(idx)

    for neighbours in self.adjMatrix:
        neighbours.pop(idx)

    self.mapVertex.pop(idx)

# Metoda usuwająca krawędź między dwoma wierzchołkami grafu.
def deleteEdge(self, vertex1, vertex2):
    idx1 = self.getVertexIdx(vertex1)
    idx2 = self.getVertexIdx(vertex2)

    self.adjMatrix[idx1][idx2] = self.initialEdgeSpecifier  # ustawiamy wartość krawędzi między wierzchołkami na wartość początkową
    self.adjMatrix[idx2][idx1] = self.initialEdgeSpecifier  # ustawiamy wartość krawędzi między wierzchołkami na wartość początkową

# Metoda zwracająca indeks wierzchołka na podstawie jego wartości.
def getVertexIdx(self, vertex):
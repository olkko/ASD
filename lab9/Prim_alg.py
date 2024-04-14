
class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        if isinstance(other, Node) and hasattr(other, 'key'):
            return self.key == other.key
        return False

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return f'{self.key}'

    def __repr__(self):
        return f'{self.key}'


class N_list:
    def __init__(self):
        self.adjList = {}
        self.mapVertex = []
        self.edgesWeights = []

    def edges(self):
        result = []

        for node, neighbours in self.adjList.items():
            result += [(node.key, neighbour.key) for neighbour in neighbours]

        return result

    def isEmpty(self):
        return not bool(self.adjList)

    def insertVertex(self, vertex):
        vertex = Node(vertex)

        self.adjList[vertex] = []
        self.mapVertex.append(vertex)

    def insertEdge(self, vertex1, vertex2, weight):
        vertex1 = Node(vertex1)
        vertex2 = Node(vertex2)

        if not (vertex1 in self.adjList[vertex2] and vertex2 in self.adjList[vertex1]):
            self.adjList[vertex1].append(vertex2)
            self.adjList[vertex2].append(vertex1)

        self.edgesWeights.append((vertex1, vertex2, weight))

    def deleteVertex(self, vertex):
        vertex = Node(vertex)

        del self.adjList[vertex]

        for node in self.adjList:
            if vertex in self.adjList[node]:
                self.adjList[node].remove(vertex)

        self.mapVertex.remove(vertex)

    def deleteEdge(self, vertex1, vertex2):
        vertex1 = Node(vertex1)
        vertex2 = Node(vertex2)
        self.adjList[vertex1].remove(vertex2)
        self.adjList[vertex2].remove(vertex1)

    def getVertexIdx(self, vertex):
        return self.mapVertex.index(vertex)

    def getVertex(self, vertex_id):
        return self.mapVertex[vertex_id]

    def neighboursIdx(self, vertex_id):
        vertex = self.getVertex(vertex_id)
        return [self.getVertexIdx(neighbour) for neighbour in self.adjList[vertex]]

    def neighbours(self, vertex_id):
        vertex = self.getVertex(vertex_id)
        return self.adjList[vertex]

    def order(self):
        return len(self.mapVertex)

    def size(self):
        return sum(self.adjList[node][neighbour] for node in self.adjList for neighbour in self.adjList[node]) / 2

    def connectedEdges(self, vertex_idx):
        vertex = self.getVertex(vertex_idx)

        result = []
        for edge in self.edgesWeights:
            if edge[0] == vertex:
                result.append((self.getVertexIdx(edge[1]), edge[2]))

        return result

    def prim(self):
        mstResult = N_list()
        inTree = {}
        distance = {}
        parent = {}
        inf = float('inf')

        for vertex in self.adjList:
            mstResult.insertVertex(vertex)
            inTree[vertex] = False
            distance[vertex] = inf
            parent[vertex] = None

        currentVertex = self.getVertex(0)
        sumOfWeights = 0

        while not inTree[currentVertex]:
            inTree[currentVertex] = True

            # mstResult.insertVertex(currentVertex)  # Dodaj wierzchołek do wyniku

            for neighbour_idx, weight in self.connectedEdges(self.getVertexIdx(currentVertex)):
                neighbour = self.getVertex(neighbour_idx)

                if not inTree[neighbour] and weight < distance[currentVertex]:
                    distance[currentVertex] = weight
                    parent[currentVertex] = neighbour

            nextVertex = None
            minWeight = inf

            for vertex, isInTree in inTree.items():
                if isInTree:
                    continue

                if minWeight >= distance[vertex]:
                    minWeight = distance[vertex]
                    nextVertex = vertex

            if nextVertex is None:
                break

            mstResult.insertEdge(
                currentVertex, parent[currentVertex], distance[currentVertex])
            mstResult.insertEdge(
                parent[currentVertex], currentVertex, distance[currentVertex])
            sumOfWeights += distance[currentVertex]

            currentVertex = nextVertex

        return mstResult, sumOfWeights


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.connectedEdges(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")


def main():
    graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
            ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
            ('C', 'G', 9), ('C', 'D', 3),
            ('D', 'G', 10), ('D', 'J', 18),
            ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
            ('F', 'H', 2), ('F', 'G', 8),
            ('G', 'H', 9), ('G', 'J', 8),
            ('H', 'I', 3), ('H', 'J', 9),
            ('I', 'J', 9)
            ]

    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    graph = N_list()

    for node in nodes:
        graph.insertVertex(node)

    for vertex in graf:
        graph.insertEdge(vertex[0], vertex[1], vertex[2])
        graph.insertEdge(vertex[1], vertex[0], vertex[2])

    mst, mst_weight = graph.prim()
    printGraph(mst)


if __name__ == "__main__":
    main()

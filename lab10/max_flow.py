import numpy as np


class Node:
    def __init__(self, key):
        self.key = key
    def __eq__(self, other):
        return self.key == other.key
    def __hash__(self) -> int:
        return hash(self.key)
    def __repr__(self) -> str:
        return f'{self.key}'


class Edge:
    def __init__(self, capacity, is_residual=False):
        self.is_residual = is_residual
        self.capacity = capacity
        if is_residual:
            self.residual = 0
            self.flow = -1
        else:
            self.residual = capacity
            self.flow = 0

    def __repr__(self):
        return f'{self.capacity} {self.flow} {self.residual} {self.is_residual}'


class N_list:
    def __init__(self):
        self.nodes = []
        self.mapVertex = dict()

    def is_empty(self):
        return not bool(self.adjList)
    
    def insertVertex(self, node):
        if node not in self.mapVertex.keys():
            self.mapVertex[node] = self.order()
            self.nodes.append([])

    def insertEdge(self, node1, node2, edge):
        node1_idx = self.getVertexIdx(node1)
        node2_idx = self.getVertexIdx(node2)
        self.nodes[node1_idx].append((node2_idx, edge))
        self.nodes[node2_idx].append((node1_idx, Edge(edge.capacity, True)))

    def deleteEdge(self, node1, node2):
            node1_idx = self.getVertexIdx(node1)
            node2_idx = self.getVertexIdx(node2)
            self.nodes[node1_idx] = [(x[0], x[1]) for x in self.nodes[node1_idx] if x[0] != node2_idx]

    def deleteVertex(self, node):
        node_idx = self.getVertexIdx(node)
        self.mapVertex.pop(node)
        for key in self.mapVertex:
            if self.mapVertex[key] > node_idx:
                self.mapVertex[key] -= 1
        self.nodes.pop(node_idx)
        for i in range(len(self.nodes)):
            self.nodes[i] = [(x[0], x[1] - 1) if x[1] > node_idx else x for x in self.nodes[i]]
    
    def getVertexIdx(self, node):
        return self.mapVertex[node]

    def getVertex(self, node_idx):
        for key, value in self.mapVertex.items():
            if value == node_idx:
                return key

    def getEdge(self, node1_idx, node2_idx):
        for neighbor_idx, edge in self.nodes[node1_idx]:
            if neighbor_idx == node2_idx:
                return edge
    
    def neighbors(self, node_idx):
        return self.nodes[node_idx]

    def order(self):
        l = len(self.mapVertex)
        return l

    def bfsSearch(self, start_idx):
        visited = [None] * self.order()
        parent = [None] * self.order()
        queue = [start_idx]
        visited[start_idx] = 1
        while queue:
            node = queue.pop(0)
            neighbors = [x[0] for x in self.nodes[node]]
            for neighbor in neighbors:
                if visited[neighbor] is None and self.getEdge(node, neighbor).residual > 0:
                    queue.append(neighbor)
                    visited[neighbor] = 1
                    parent[neighbor] = node
        return parent

    def pathAnalyze(self, start, end, parent):
        curr_node = end
        min_cap = np.inf
        if parent[curr_node] is None:
            return 0
        while curr_node != start:
            for neighbor_idx, edge in self.nodes[parent[curr_node]]:
                if neighbor_idx == curr_node and not edge.is_residual:
                    min_cap = min(edge.residual, min_cap)
                    break
            curr_node = parent[curr_node]
        return min_cap

    def augmentation(self, start, end, parent, min_cap):
        curr_node = end
        while curr_node != start:
            self.getEdge(parent[curr_node], curr_node).flow += min_cap
            self.getEdge(parent[curr_node], curr_node).residual -= min_cap
            self.getEdge(curr_node, parent[curr_node]).residual += min_cap
            curr_node = parent[curr_node]

    def FordFulkerson(self):
        start = self.getVertexIdx(Node('s'))
        end = self.getVertexIdx(Node('t'))
        parent = self.bfsSearch(start)
        capacity = self.pathAnalyze(start, end, parent)
        flow_sum = 0
        while capacity > 0:
            flow_sum += capacity
            self.augmentation(start, end, parent, capacity)
            parent = self.bfsSearch(start)
            capacity = self.pathAnalyze(start, end, parent)
        return flow_sum


def print_graph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        node = g.getVertex(i)
        print(node, end=" -> ")
        neighbors = g.neighbors(i)
        for (j, edge) in neighbors:
            neighbor_node = g.getVertex(j)
            print(neighbor_node, edge, end=";")
        print()
    print("-------------------")


graph_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
graph_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20),
          ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
graph_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
          ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
graph_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
          ('d', 'c', 4)]

def print_graph_info(counter, flow):
    print("Graph " + str(counter) + ", maximum flow found: " + str(flow))

counter = 1
for graph in [graph_0, graph_1, graph_2, graph_3]:
    test = N_list()
    for edge_info in graph:
        node1 = Node(edge_info[0])
        node2 = Node(edge_info[1])
        test.insertVertex(node1)
        test.insertVertex(node2)
        capacity = edge_info[2]
        test.insertEdge(node1, node2, Edge(capacity))
    
    print_graph_info(counter, test.FordFulkerson())
    print_graph(test)
    counter += 1

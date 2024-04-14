import numpy as np
import copy as cp
import itertools as it


class GraphAdjMat:
    def __init__(self, initialEdgeSpecifier=0):
        self.adjMatrix = []
        self.mapVertex = []
        self.initialEdgeSpecifier = initialEdgeSpecifier

    def edges(self):
        result = []
        for node_id, neighbours in enumerate(self.adjMatrix):
            for neighbour_id, neighbour in enumerate(neighbours):
                if neighbour is not self.initialEdgeSpecifier:
                    result.append((self.getVertex(node_id).key, self.getVertex(neighbour_id).key))
        return result

    def isEmpty(self):
        return not bool(self.adjMatrix)

    def insertVertex(self, vertex):
        self.mapVertex.append(Node(vertex))

        new_order = self.order() + 1

        for neighbours in self.adjMatrix:
            neighbours.append(self.initialEdgeSpecifier)

        self.adjMatrix.append([self.initialEdgeSpecifier for i in range(new_order)])

    def insertEdge(self, vertex1, vertex2, edge):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)

        self.adjMatrix[idx1][idx2] = 1
        self.adjMatrix[idx2][idx1] = 1

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)

        self.adjMatrix.pop(idx)

        for neighbours in self.adjMatrix:
            neighbours.pop(idx)

        self.mapVertex.pop(idx)

    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)

        self.adjMatrix[idx1][idx2] = self.initialEdgeSpecifier
        self.adjMatrix[idx2][idx1] = self.initialEdgeSpecifier

    def getVertexIdx(self, vertex):
        return self.mapVertex.index(Node(vertex))

    def getVertex(self, vertex_idx):
        return self.mapVertex[vertex_idx]

    def neighboursIdx(self, vertex_idx):
        return [self.getVertexIdx(neighbour) for neighbour in self.adjMatrix[vertex_idx]]

    def neighbours(self, vertex_idx):
        return self.adjMatrix[vertex_idx]

    def order(self):
        return len(self.adjMatrix)

    def size(self):
        result = 0
        for neighbours in self.adjMatrix:
            for neighbour in neighbours:
                result += 1 if neighbour is not self.initialEdgeSpecifier else 0
        return result


class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return f'{self.key}'


def deg_of_node(list_of_edges):
    return sum([elem == 1 for elem in list_of_edges])


def create_m0_matrix(matrix_shape, g_adj_matrix, p_adj_matrix):
    m0_matrix = np.zeros(matrix_shape)

    for p_node, g_node in it.product(range(matrix_shape[0]), range(matrix_shape[1])):
        if deg_of_node(p_adj_matrix[p_node, :]) <= deg_of_node(g_adj_matrix[g_node, :]):
            m0_matrix[p_node, g_node] = 1

    return m0_matrix


def prune(p_adj_matrix, g_adj_matrix, matrix):
    matrix_changed = True

    while matrix_changed:
        matrix_changed = False

        for p_node, g_node in it.product(range(matrix.shape[0]), range(matrix.shape[1])):
            if matrix[p_node, g_node] != 1:
                continue

            break_satisfied = False

            for x, y in it.product(p_adj_matrix[p_node], g_adj_matrix[g_node]):
                if matrix[x][y] == 1:
                    break_satisfied = True
                    break

            if break_satisfied:
                matrix[p_node, g_node] = 0
                matrix_changed = True

    return matrix_changed


def ullman1_0(p_adj_matrix, g_adj_matrix, matrix_shape=None, matrix=None, current_row=None, usage_of_columns=None,
              num_of_recursive_calls=0, num_of_isomorphisms=0):
    num_of_recursive_calls += 1

    if matrix_shape is not None:  
        matrix = np.zeros(matrix_shape)

    if current_row is None:
        current_row = 0

    if usage_of_columns is None:
        usage_of_columns = [False] * matrix.shape[1]

    matrix_cp = cp.copy(matrix)

    if current_row == matrix.shape[0]:
        if np.all(p_adj_matrix == matrix_cp @ ((matrix_cp @ g_adj_matrix).transpose())):
            num_of_isomorphisms += 1

            return num_of_isomorphisms, num_of_recursive_calls

        else:
            return num_of_isomorphisms, num_of_recursive_calls

    for i in range(len(usage_of_columns)):
        if not usage_of_columns[i]:
            usage_of_columns[i] = True

            matrix_cp[current_row, :] = np.zeros((1, matrix.shape[1]))
            matrix_cp[current_row, i] = 1

            num_of_isomorphisms, num_of_recursive_calls = ullman1_0(p_adj_matrix=p_adj_matrix,
                                                                    g_adj_matrix=g_adj_matrix,
                                                                    matrix=matrix_cp,
                                                                    current_row=current_row + 1,
                                                                    usage_of_columns=usage_of_columns,
                                                                    num_of_recursive_calls=num_of_recursive_calls,
                                                                    num_of_isomorphisms=num_of_isomorphisms)

            usage_of_columns[i] = False

    return num_of_isomorphisms, num_of_recursive_calls


def ullman2_0(p_adj_matrix, g_adj_matrix, matrix_shape=None, matrix=None, m0_matrix=None, current_row=None,
              usage_of_columns=None, num_of_recursive_calls=0, num_of_isomorphisms=0):
    num_of_recursive_calls += 1

    if matrix_shape is not None:  # entering this if means it is the first call of the function
        matrix = np.zeros(matrix_shape)
        m0_matrix = create_m0_matrix(matrix_shape=matrix_shape, g_adj_matrix=g_adj_matrix, p_adj_matrix=p_adj_matrix)

    if current_row is None:
        current_row = 0

    if usage_of_columns is None:
        usage_of_columns = [False] * matrix.shape[1]

    matrix_cp = cp.copy(matrix)

    if current_row == matrix.shape[0]:
        if np.all(p_adj_matrix == matrix_cp @ ((matrix_cp @ g_adj_matrix).transpose())):
            num_of_isomorphisms += 1

            return num_of_isomorphisms, num_of_recursive_calls

        else:
            return num_of_isomorphisms, num_of_recursive_calls

    for i in range(len(usage_of_columns)):
        if not usage_of_columns[i] and m0_matrix[current_row][i]:
            usage_of_columns[i] = True

            matrix_cp[current_row, :] = np.zeros((1, matrix.shape[1]))
            matrix_cp[current_row, i] = 1

            num_of_isomorphisms, num_of_recursive_calls = ullman2_0(p_adj_matrix=p_adj_matrix,
                                                                    g_adj_matrix=g_adj_matrix,
                                                                    matrix=matrix_cp,
                                                                    current_row=current_row + 1,
                                                                    m0_matrix=m0_matrix,
                                                                    usage_of_columns=usage_of_columns,
                                                                    num_of_recursive_calls=num_of_recursive_calls,
                                                                    num_of_isomorphisms=num_of_isomorphisms)

            usage_of_columns[i] = False

    return num_of_isomorphisms, num_of_recursive_calls


def ullman3_0(p_adj_matrix, g_adj_matrix, matrix_shape=None, matrix=None, m0_matrix=None, current_row=None,
              usage_of_columns=None, num_of_recursive_calls=0, num_of_isomorphisms=0):
    num_of_recursive_calls += 1

    if matrix_shape is not None:  # entering this if means it is the first call of the function
        matrix = np.zeros(matrix_shape)
        m0_matrix = create_m0_matrix(matrix_shape=matrix_shape, g_adj_matrix=g_adj_matrix, p_adj_matrix=p_adj_matrix)

    if current_row is None:
        current_row = 0

    if usage_of_columns is None:
        usage_of_columns = [False] * matrix.shape[1]

    matrix_cp = cp.copy(matrix)

    if current_row == matrix.shape[0]:
        if np.all(p_adj_matrix == matrix_cp @ ((matrix_cp @ g_adj_matrix).transpose())):
            num_of_isomorphisms += 1

            return num_of_isomorphisms, num_of_recursive_calls

        else:
            return num_of_isomorphisms, num_of_recursive_calls

    was_pruned = prune(p_adj_matrix=p_adj_matrix, g_adj_matrix=g_adj_matrix, matrix=matrix_cp)

    for i in range(len(usage_of_columns)):
        if not usage_of_columns[i] and m0_matrix[current_row][i] and not was_pruned:
            usage_of_columns[i] = True

            matrix_cp[current_row, :] = np.zeros((1, matrix.shape[1]))
            matrix_cp[current_row, i] = 1

            num_of_isomorphisms, num_of_recursive_calls = ullman3_0(p_adj_matrix=p_adj_matrix,
                                                                    g_adj_matrix=g_adj_matrix,
                                                                    matrix=matrix_cp,
                                                                    current_row=current_row + 1,
                                                                    m0_matrix=m0_matrix,
                                                                    usage_of_columns=usage_of_columns,
                                                                    num_of_recursive_calls=num_of_recursive_calls,
                                                                    num_of_isomorphisms=num_of_isomorphisms)

            usage_of_columns[i] = False

    return num_of_isomorphisms, num_of_recursive_calls



if __name__ == "__main__":
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    g = GraphAdjMat()
    p = GraphAdjMat()

    for node_letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        g.insertVertex(node_letter)

    for node_letter in ['A', 'B', 'C']:
        p.insertVertex(node_letter)

    for edge in graph_G:
        g.insertEdge(edge[0], edge[1], edge[2])

    for edge in graph_P:
        p.insertEdge(edge[0], edge[1], edge[2])

    mat_g = np.array(g.adjMatrix)
    mat_p = np.array(p.adjMatrix)

    num_of_isomorphisms1, num_of_recursive_calls1 = ullman1_0(p_adj_matrix=mat_p, g_adj_matrix=mat_g,
                                                              matrix_shape=(mat_p.shape[0], mat_g.shape[0]))
    print(f'\nisomorphisms Ullman1.0 algorithm: {num_of_isomorphisms1}')
    print(f'calls Ullman1.0 algorithm: {num_of_recursive_calls1}')

    num_of_isomorphisms2, num_of_recursive_calls2 = ullman2_0(p_adj_matrix=mat_p, g_adj_matrix=mat_g,
                                                              matrix_shape=(mat_p.shape[0], mat_g.shape[0]))
    print(f'\nisomorphisms Ullman2.0 algorithm: {num_of_isomorphisms2}')
    print(f'calls Ullman2.0 algorithm: {num_of_recursive_calls2}')

    num_of_isomorphisms3, num_of_recursive_calls3 = ullman3_0(p_adj_matrix=mat_p, g_adj_matrix=mat_g,
                                                              matrix_shape=(mat_p.shape[0], mat_g.shape[0]))
    print(f'\nisomorphisms Ullman3.0 algorithm: {num_of_isomorphisms3}')
    print(f' calls Ullman3.0 algorithm: {num_of_recursive_calls3}')

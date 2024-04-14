import numpy as np
import turtle

class Node:
    def __init__(self, key):
        self.key = key
    def __eq__(self, other):
        return self.key == other.key
    def __hash__(self) -> int:
        return hash(self.key)
    def __str__(self):
        return f'{self.key}'

class N_mat:
    def  __init__(self, val = 0):
        self.adjMatrix = []
        self.mapVertex = []
        self.val = val

    def isEmpty(self) ->bool:
        return not bool(self.adjMatrix)
    
    def insertVertex(self, vertex):
        self.mapVertex.append(Node(vertex))
        order_n = self.order()+1
        for neighbours in self.adjMatrix:
            neighbours.append(self.val)
        self.adjMatrix.append([self.val for i in range(order_n)]) 
        
    def insertEdge(self, vertex1, vertex2):
        vertex_1 = self.getVertexIdx(vertex1)
        vertex_2 = self.getVertexIdx(vertex2)

        self.adjMatrix[vertex_1][vertex_2] = 1
        self.adjMatrix[vertex_2][vertex_1] = 1

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)

        self.adjMatrix.pop(idx)

        for neighbours in self.adjMatrix:
            neighbours.pop(idx)

        self.mapVertex.pop(idx)
        
    def deleteEdge(self, vertex1, vertex2):
        vertex1 = self.getVertexIdx(vertex1)
        vertex2 = self.getVertexIdx(vertex2)

        self.adjMatrix[vertex1][vertex2] = self.val
        self.adjMatrix[vertex2][vertex1] = self.val

    def getVertexIdx(self, vertex):
        return self.mapVertex.index(Node(vertex))
    
    def getVertex(self, vertex_idx):
        return self.mapVertex(vertex_idx)
    
    def neighbourIdx(self, vertex_idx):
        return [self.getVertexIdx(neighbour) for neighbour in self.adjMatrix[vertex_idx]]

    def neighbour(self, vertex_idx):
        return self.adjMatrix(vertex_idx)
    
    def order(self):
        l = len(self.adjMatrix)
        return l

    def edges(self):
            result = []
            for i in range(self.order()):
                for j in range(self.order()):
                    if self.adjMatrix[i][j] != self.val:
                        result.append((self.getVertex(i).key, self.getVertex(j).key))
            return result
    
    def ullman(act_w ,mat_M):
        used_list = [0 for i in range(len(mat_M[:0]))]
        if act_w == len(mat_M[:0]):
            print(mat_M)
            return
        for c in mat_M:
            if used_list[c] is False:
                used_list[c] = True
                for w in range(act_w):
                    act_w[w] = 0
                    


    


if __name__ == "__main__":    
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]  

    G = N_mat()
    P = N_mat()

    G = np.array(graph_G)
    P = np.array(graph_P)

    M = np.array()
    

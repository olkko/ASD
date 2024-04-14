
class Macierz:
    def __init__(self, arg, value=0):
        if isinstance(arg, tuple): 
            self.rows, self.cols = arg 
            self.data = [[value]*self.cols for _ in range(self.rows)] 
        else: 
            self.rows = len(arg) 
            self.cols = len(arg[0]) 
            self.data = arg 

    def __getitem__(self, idx):
        return self.data[idx] 

    def __str__(self):
        return "\n".join(["| " + "  ".join([str(x) for x in row]) + " |" for row in self.data]) 

    def __mul__(self, other):
        if self.cols != other.rows: 
            return None

        result = Macierz((self.rows, other.cols)) 
        for i in range(result.rows):
            for j in range(result.cols):
                result[i][j] = sum([self[i][k] * other[k][j] for k in range(self.cols)]) 

        return result

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols: 
            return None

        result = Macierz((self.rows, self.cols)) 
        for i in range(result.rows):
            for j in range(result.cols):
                result[i][j] = self[i][j] + other[i][j] 
        return result

    def size(self):
        return (self.rows, self.cols)

def transpose(matrix):
    result = Macierz((matrix.cols, matrix.rows)) 
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            result[j][i] = matrix[i][j] 

    return result

def main():
    m1 = Macierz([[1, 0, 2], [-1, 3, 1]])

    m2 = Macierz((3, 2), value=1)

    m3 = Macierz([[3, 1], [2, 1], [1, 0]])
    print('transpozycja macierzy')
    print(transpose(m1))
    print('suma macierzy z macierzą')
    print(m1 * m3)
    print('mnożenie macierzy przez macierz')
    print(m1 + m2)

    
if __name__ == '__main__':
    main()
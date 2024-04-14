
class Macierz:
    def __init__(self, arg, value=0):
        if isinstance(arg, tuple): # jeśli argument to krotka
            self.rows, self.cols = arg # to argument określa rozmiary macierzy
            self.data = [[value]*self.cols for _ in range(self.rows)] # tworzymy macierz wypełnioną wartością value
        else: # w przeciwnym wypadku arg to lista list
            self.rows = len(arg) # określamy liczbę wierszy
            self.cols = len(arg[0]) # określamy liczbę kolumn
            self.data = arg # wewnętrzne reprezentowanie macierzy to przekazana lista list

    def __getitem__(self, idx):
        return self.data[idx] # pozwalamy na dostęp do macierzy jak w C: m[i][j]

    def __str__(self):
        return "\n".join(["| " + "  ".join([str(x) for x in row]) + " |" for row in self.data]) # wypisujemy macierz

    def __mul__(self, other):
        if self.cols != other.rows: # jeśli liczba kolumn pierwszej macierzy jest różna od liczby wierszy drugiej macierzy, to nie można ich pomnożyć
            raise ValueError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy")

        result = Macierz((self.rows, other.cols)) # tworzymy nową macierz wynikową
        for i in range(result.rows):
            for j in range(result.cols):
                result[i][j] = sum([self[i][k] * other[k][j] for k in range(self.cols)]) # liczymy każdy element macierzy wynikowej jako sumę iloczynów elementów z odpowiednich wierszy i kolumn

        return result

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols: # jeśli rozmiary macierzy są różne, to nie można ich dodać
            raise ValueError("Macierze muszą być tego samego rozmiaru")

        result = Macierz((self.rows, self.cols)) # tworzymy nową macierz wynikową
        for i in range(result.rows):
            for j in range(result.cols):
                result[i][j] = self[i][j] + other[i][j] # sumujemy elementy macierzy

        return result

    def size(self):
        return (self.rows, self.cols)

def transpose(matrix):
    result = Macierz((matrix.cols, matrix.rows)) # tworzymy nową macierz wynikową
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            result[j][i] = matrix[i][j] # przepisujemy elementy z macierzy wejściowej do macierzy wynikowej w transponowanej postaci

    return result

def main():
    m1 = Macierz([[1, 0, 2], [-1, 3, 1]])

    m2 = Macierz((3, 2), value=1)

    m3 = Macierz([[3, 1], [2, 1], [1, 0]])

    print(transpose(m1))
    print(m1 * m3)
    print(m1 + m2)

if __name__ == '__main__':
    main()
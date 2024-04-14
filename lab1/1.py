class Macierz:
    def __init__(self, arg, fill_value=0):
        if isinstance(arg, tuple):  # jeżeli argumentem jest krotka (rozmiar macierzy)
            self.nrows, self.ncols = arg  # to ustawiamy liczbę wierszy i kolumn
            self._data = [[fill_value] * self.ncols for _ in range(self.nrows)]  # i inicjujemy pustą macierz wypełnioną wartością domyślną
        else:  # w przeciwnym przypadku (argument to lista list)
            self._data = arg  # to przypisujemy go bezpośrednio jako wewnętrzną reprezentację macierzy
            self.nrows = len(arg)  # i ustawiamy liczbę wierszy na długość tej listy
            self.ncols = len(arg[0])  # a liczbę kolumn na długość pierwszego wiersza

    def __str__(self):
        return "\n".join(["| " + "  ".join([str(self._data[i][j]) for j in range(self.ncols)]) + " |" for i in range(self.nrows)])
        # Tworzymy string reprezentujący naszą macierz, w którym kolejne wiersze są oddzielane znakiem nowej linii
        # Dla każdego wiersza tworzymy "górną belkę" (znak "|"), potem oddzielamy kolejne elementy wiersza spacją, korzystając z pętli wewnętrznej i join
        # Na końcu tworzymy "dolną belkę" i łączymy powstałe trzy elementy

    def __getitem__(self, key):
        return self._data[key]
        # Zwracamy wiersz o numerze key, który jest kluczem, którego użyto w []-ach

    def __add__(self, other):
        if (self.nrows != other.nrows) or (self.ncols != other.ncols):  # Sprawdzamy, czy macierze mają takie same rozmiary
            raise ValueError("Macierze muszą mieć takie same rozmiary")
        result = Macierz((self.nrows, self.ncols))  # Tworzymy nową macierz o takich samych rozmiarach jak nasze macierze wejściowe
        for i in range(self.nrows):  # Dla każdego wiersza
            for j in range(self.ncols):  # i każdej kolumny
                result[i][j] = self._data[i][j] + other[i][j]  # Obliczamy sumę dwóch odpowiadających sobie elementów i wpisujemy ją do nowej macierzy
        return result

    def __mul__(self, other):
        if self.ncols != other.nrows:  # Sprawdzamy, czy liczba kolumn pierwszej macierzy jest równa liczbie wierszy drugiej macierzy
            raise ValueError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy")
        result = Macierz((self.nrows, other.ncols))  #
        for i in range(result.rows):
            for j in range(result.cols):
                result[i][j] = self[i][j] + other[i][j] # sumujemy elementy macierzy

        return result

    def size(self):
        return (self.rows, self.cols)

def transpose(matrix):
    result = Macierz((matrix.ncols, matrix.nrows)) # tworzymy nową macierz wynikową
    for i in range(matrix.nrows):
        for j in range(matrix.ncols):
            result[j][i] = matrix[i][j] # przepisujemy elementy z macierzy wejściowej do macierzy wynikowej w transponowanej postaci

    return result

def main():
    m1 = Macierz([[1, 0, 2], [-1, 3, 1]])

    m2 = Macierz((3, 2), fill_value=1)

    m3 = Macierz([[3, 1], [2, 1], [1, 0]])

    print(transpose(m1))
    print(m1 * m3)
    print(m1 + m2)

if __name__ == '__main__':
    main()
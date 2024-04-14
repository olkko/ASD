class Hash_tab:
    def  __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2

    def search(self, key):
        i = 0
        while i < len(self.tab):
            j = self.probkowanie(key, i)
            if self.tab[j] is None:
                return None
            elif self.tab[j][0] == key:
                return self.tab[j][1]
            else:
                i += 1
        return None

    def insert(self, key, value):
        i = 0
        while i < len(self.tab):
            j = self.probkowanie(key, i)
            if self.tab[j] is None or self.tab[j][0] == key:
                self.tab[j] = (key, value)
                return
            else:
                i += 1
        print("Table is full")

    def remove(self, key):
        i = 0
        while i < len(self.tab):
            j = self.probkowanie(key, i)
            if self.tab[j] is None:
                return None
            elif self.tab[j][0] == key:
                self.tab[j] = None
                return
            else:
                i += 1
        return None

    def __str__(self):
        return str(self.tab)

    def mieszanie(self, n):
        if isinstance(n, str):
            length = len(n)
            result = 0
            for i in range(length):
                result += ord(n[i])
            n = result
            return n
        if isinstance(n, int):
            return n
        else:
            return None

    def size_modul(self):
        return len(self.tab)

    def probkowanie(self, key, i):
        h = self.mieszanie(key)
        return (h + self.c1 * i + self.c2 * i * i) % len(self.tab)


def test1():
    hash_t = Hash_tab(13, 1, 0)
    keys = [1, 2, 3, 4, 5, 18, 31, 8, 9, 10, 11, 12, 13, 14, 15]
    values = ['A', 'B', 'C', 'D', 'E', 'R', 'Z', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

    for i in range(len(keys)):
        hash_t.insert(keys[i], values[i])

    print(hash_t)

    print(hash_t.search(5))

    print(hash_t.search(14))

    hash_t.insert(5, 'Z')

    print(hash_t.search(5))

    hash_t.remove(5)

    print(hash_t)

    print(hash_t.search(31))


def test2():
    hash_t = Hash_tab(13, 1, 0)
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

    for i in range(len(values)):
        hash_t.insert(str(i * 13 + 13), values[i])

    print(hash_t)


if __name__ == "__main__":
    test1()
    test2()

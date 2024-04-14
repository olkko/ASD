def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]

class CyclTable:
    def  __init__(self):
        self.tab = realloc([], 5)
        self.read = 0
        self.write = 0

    def is_empty(self):
        if self.read == self.write:
            return True
        else: 
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.read]


    def dequeue(self):
        if self.is_empty():
            return None
        else:
            result = self.tab[self.read]
            self.tab[self.read] = None
            self.read +=1
            return result
        
    def enqueue(self, data):
        self.tab[self.write] = data
        self.write += 1
        if self.write == len(self.tab):
            self.write = 0
        if self.write == self.read:
            self.tab = realloc(self.tab, len(self.tab) * 2)
            if self.write < self.read:
                self.tab[self.write:] = self.tab[:len(self.tab) // 2]
                self.write += len(self.tab) // 2
            else:
                self.tab[self.read + len(self.tab) // 2:self.read + len(self.tab)] = self.tab[self.read:]
                self.write = self.read + len(self.tab) // 2
        # update self.read pointer after resizing self.tab
        if self.read == len(self.tab):
            self.read = 0


    def __str__ (self):
        if self.is_empty():
            return '[]'
        else:
            return str([self.tab[(self.read+i) % len(self.tab)] for i in range(len(self.tab)) if self.tab[(self.read+i) % len(self.tab)] is not None])



def main():
    queue = CyclTable()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    first = queue.dequeue()
    print(f"Pierwsza liczba: {first}")
    second = queue.peek()
    print(f"Druga liczba: {second}")
    print(f"Aktualny stan: {queue}")

    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)

    print(f"Aktualny stan tablicy: {queue.tab}")

    while not queue.is_empty():
        data = queue.dequeue()
        print(f"Usunieto: {data}")

    print(f"Pusta kolejka: {queue}")

if __name__ == '__main__':
    main()
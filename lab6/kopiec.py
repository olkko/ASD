class Kopiec:
    def  __init__(self):
        self.tab = []
        self.heap_size = 0

    def is_empty(self) ->bool:
        return self.heap_size == 0  

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0]

    def dequeue(self):
        if self.is_empty():
            return None
        element = self.tab[0]
        self.tab[0] = self.tab[-1]
        self.tab.pop()
        self.heap_size -= 1
        self.max_heapify(0)
        return element

    def enqueue(self, elem):
        if self.heap_size < len(self.tab):
            self.tab[self.heap_size] = elem
        else:
            self.tab.append(elem)
        self.heap_size += 1
        self.sift_up(self.heap_size - 1) # przesiewanie w górę dla dodanego elementu

    def left(self, i):
        return ((2*i)+1)
    
    def right(self, i):
        return ((2*i)+2)
    
    def parent(self, i):
        return (i-1) // 2
    

    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<self.heap_size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.heap_size and self.tab[l] > self.tab[i]:
            largest = l
        if r < self.heap_size and self.tab[r] > self.tab[largest]:
            largest = r
        if largest != i:
            self.tab[i], self.tab[largest] = self.tab[largest], self.tab[i]
            self.max_heapify(largest)

    def sift_up(self, i):
        parent = self.parent(i)
        while i > 0 and self.tab[i] > self.tab[parent]:
            self.tab[i], self.tab[parent] = self.tab[parent], self.tab[i]
            i = parent
            parent = self.parent(i)

class Record:
    def __init__(self, data, priorytet):
        self.priorytet = priorytet
        self.data = data

    def __lt__(self, other):
        return self.priorytet < other.priorytet

    def __gt__(self, other):
        return self.priorytet > other.priorytet

    def __str__(self):
        return str(self.priorytet) + ":" + str(self.data)  
def main():
    queue = Kopiec() 
    lista = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    napis = "GRAMOTYLA"
    for i in range(len(lista)):
        r = Record(napis[i], lista[i])
        queue.enqueue(r)
    queue.print_tree(0,0)
    queue.print_tab()
    
    pierwsza_dana = queue.dequeue()
    p = queue.peek()
    print(p)
    queue.print_tab()
    print(pierwsza_dana)
    while not queue.is_empty():
        print(queue.dequeue())
    queue.print_tab()


if __name__ == "__main__":
    main()
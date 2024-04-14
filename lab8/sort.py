import time
import random
class Kopiec:
    def  __init__(self, lista = None):
        self.tab = []
        self.heap_size = 0
        if lista is not None:
            self.tab = lista
            self.heap_size = len(lista)
            for i in range(self.heap_size-1, 0, -1):
                parent = self.parent(i)
                self.max_heapify(parent)

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
        element = self.peek()
        self.tab[0] = self.tab[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)  
        return element

    def enqueue(self, elem):
        if self.heap_size < len(self.tab):
            self.tab[self.heap_size] = elem
        else:
            self.tab.append(elem)
        self.heap_size += 1
        self.sift_up(self.heap_size - 1) 
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
        if r < self.heap_size and (self.tab[r] > self.tab[largest] or (self.tab[r] == self.tab[largest] and r < largest)):
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
    
def sortSwap(unsortedlist):
        for i in range(len(unsortedlist)):
            id = i
            for j in range(i+1, len(unsortedlist)):
                if unsortedlist[j] < unsortedlist[id]:
                    id = j
            unsortedlist[i], unsortedlist[id] = unsortedlist[id], unsortedlist[i]
        return unsortedlist
    


def sortShift(unsortedlist):
    for i in range(len(unsortedlist)):
        id = i
        for j in range(i+1, len(unsortedlist)):
            if unsortedlist[j] < unsortedlist[id]:
                id = j
        deleted = unsortedlist.pop(id)
        unsortedlist.insert(i, deleted)
    return unsortedlist


class Record:
    def __init__(self, data, priorytet):
        self.priorytet = priorytet
        self.data = data

    def __lt__(self, other):
        if self.priorytet == other.priorytet:
            return self.data < other.data
        return self.priorytet < other.priorytet  
    def __gt__(self, other):
        return self.priorytet > other.priorytet  

    def __repr__(self):
        return str(self.priorytet) + ":" + str(self.data)  
def test1():
    dane = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1,'I'), (2,'J')]
    record_list = [Record(elem[1], elem[0]) for elem in dane]

    kopiec = Kopiec(record_list)

    kopiec.print_tab()
    kopiec.print_tree(0, 0)

    posortowane = []
    while not kopiec.is_empty():
        posortowane.append(kopiec.dequeue())
    print([elem.data for elem in posortowane])

def test2():
    tab = [int(random.random() * 100) for i in range(10000)]
    kopiec = Kopiec()
    for elem in tab:
        kopiec.enqueue(Record(elem, elem))

    t_start = time.perf_counter()
    for i in range(len(tab)):
        tab[i] = kopiec.dequeue().data
    t_stop = time.perf_counter()
    time_usual = t_stop - t_start
    print("Czas sortowania:", "{:.7f}".format(time_usual))

def test3():
    dane = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1,'I'), (2,'J')]
    sortedSwap = sortSwap(dane)
    print(sortedSwap)
    sortedShift = sortShift(dane)
    print(sortedShift)

def test4():
    tab = [int(random.random() * 100) for i in range(10000)]

    t_start = time.perf_counter()
    sortSwap(tab.copy())
    t_stop = time.perf_counter()
    time_Swap = t_stop - t_start
    print("Czas sortowania Swap:", "{:.7f}".format(time_Swap))

    t_start = time.perf_counter()
    sortShift(tab)
    t_stop = time.perf_counter()
    time_Shift = t_stop - t_start
    print("Czas sortowania Shift:", "{:.7f}".format(time_Shift))


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
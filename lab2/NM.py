class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
        
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
        
    def add(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        
    def remove(self):
        if self.head is None:
            raise Exception("List is empty")
        self.head = self.head.next
        
    def remove_end(self):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        
    def get(self):
        if self.head is None:
            raise Exception("List is empty")
        return self.head.data
        
    def destroy(self):
        self.head = None
        
    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += "-> " + str(current.data) + "\n"
            current = current.next
        return result
def main():
    uczelnia = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]

    # utwórz listę wiązaną z pierwszych 3 uczelni używając dodawania na koniec
    uczelnie = LinkedList()
    uczelnie.append(uczelnia[0])
    uczelnie.append(uczelnia[1])
    uczelnie.append(uczelnia[2])
    print(uczelnie)

    # dołącz do listy wiązanej kolejne uczelnie używając dodawania na początek listy
    uczelnie.add(uczelnia[3])
    uczelnie.add(uczelnia[4])
    uczelnie.add(uczelnia[5])

    # wypisz listę
    print(uczelnie)

    # wypisz długość listy
    print("Length:", uczelnie.length())

    # usuń z listy pierwszy element
    uczelnie.remove()

    # wypisz pierwszy element z listy
    print("First element:", uczelnie.get())

    # usuń z listy ostatni element
    uczelnie.remove_end()

    # wypisz listę
    print(uczelnie)

    # usuń całą listę i wypisz wynik is_empty dla usuniętej listy
    uczelnie.destroy()
    print("Is empty:", uczelnie.is_empty())

# wywołaj usu
if __name__ == '__main__':
    main()
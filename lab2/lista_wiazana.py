class DataElem:
    def __init__(self, data):
        self.data = data
        self.next = None

class BList:
    def __init__(self):
        self.head = None

    def destroy (self):
        self.head = None

    def add (self, data):
        new_node = DataElem(data)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, data):
        new_node = DataElem(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove(self):
        if self.head is not None:
            self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return None
        current_elem = self.head
        next_elem = current_elem.next
        while next_elem.next is not None:
            current_elem = current_elem.next
            next_elem = next_elem.next

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def length(self):
        current_elem = self.head
        count = 0
        while current_elem is not None:
            count+=1
            current_elem = current_elem.next
        return count
    
    def get(self):
        if self.head is None:
            return None
        return self.head.data

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += "-> " + str(current.data) + "\n"
            current = current.next
        return result


    
def main():
    lst = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]

    uczelnie = BList()
    uczelnie.append(lst[0])
    uczelnie.append(lst[1])
    uczelnie.append(lst[2])

    uczelnie.add(lst[3])
    uczelnie.add(lst[4])
    uczelnie.add(lst[5])

    print(uczelnie)
    print("Length: ",uczelnie.length(), "\n")

    uczelnie.remove()

    print("First element: \n",uczelnie.get(), "\n")

    uczelnie.remove_end()
    print("After remove_end: \n", uczelnie)

    uczelnie.destroy()
    print("Is empty: ", uczelnie.is_empty())
  
if __name__ == '__main__':
    main()
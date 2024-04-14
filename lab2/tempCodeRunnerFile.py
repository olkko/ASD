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
    print(uczelnie)
if __name__ == '__main__':
    main()
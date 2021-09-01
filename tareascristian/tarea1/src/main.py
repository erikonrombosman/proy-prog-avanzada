from doublylinkedlist.DoublyLinkedList import DoublyLinkedList


def main():
    lista = DoublyLinkedList()
    print(lista.is_emtpy())
    lista.add_first(10)
    lista.add_last(20)
    lista.add_first(40)
    print(lista.last.get_dato())
    # for i in range(lista.size()):
    #    print(lista.get(i))
    lista.add_after(20, 28)
    print(lista.size())
    lista.add_before(20, 60)

    print(lista.__str__())
    lista.remove(29)
    print(lista.__str__())
    print(lista.first.get_dato())
    print(lista.last.get_dato())
    """
    for i in range(lista.size()):
        print(lista.get(i))
    indice = lista.contains(66)
    print(f"El indice es: {indice}")
    
    print(lista.first.get_dato())
    print(lista.clear())
    print(lista.is_emtpy())
    print(lista.__str__())
    """


main()

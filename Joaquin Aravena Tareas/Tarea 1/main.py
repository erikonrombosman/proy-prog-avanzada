from doublyLinkedList import DoublyLinkedList

lista = DoublyLinkedList()
lista.add_first(10)
lista.add_last(20)
lista.add_first(40)
lista.add_last(30)
print(lista.__str__())
print(lista.contains(30))
lista.add_after(10, 25)
lista.add_before(10, 35)
print(lista.__str__())
lista.remove_first()
lista.remove_last()
lista.remove(10)
print(lista.__str__())
lista.clear()
print(lista.contains(10))
print(lista.__str__())

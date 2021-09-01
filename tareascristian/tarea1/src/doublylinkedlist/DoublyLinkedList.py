from doublylinkedlistitem.DoublyLinkedListItem import DoublyLinkedListItem


class DoublyLinkedList:
    first: DoublyLinkedListItem
    last: DoublyLinkedListItem
    cant: int

    def __init__(self) -> None:
        self.cant = 0
        self.last = None
        self.first = None

    def add_first(self, dato: object) -> None:
        nuevo = DoublyLinkedListItem(dato)
        if self.is_emtpy():
            self.first = nuevo
            self.last = nuevo
            self.first.set_next(self.last)
            self.first.set_previous(self.last)
            self.last.set_next(self.first)
            self.last.set_previous(self.first)
            self.cant += 1
        else:
            nuevo.set_next(self.first)
            nuevo.set_previous(self.last)
            self.first.set_previous(nuevo)
            self.last.set_next(nuevo)
            self.first = nuevo
            self.cant += 1

    def add_last(self, dato: object) -> None:
        nuevo = DoublyLinkedListItem(dato)
        if self.is_emtpy():
            self.first = nuevo
            self.last = nuevo
            self.first.set_next(self.last)
            self.first.set_previous(self.last)
            self.last.set_next(self.first)
            self.last.set_previous(self.first)
            self.cant += 1
        else:
            self.last.set_next(nuevo)
            nuevo.set_previous(self.last)
            nuevo.set_next(self.first)
            self.first.set_previous(nuevo)
            self.last = nuevo
            self.cant += 1

    def add_after(self, dato: object, dato_after: object) -> None:
        if self.get(self.contains(dato)) == self.last:
            self.add_last(dato_after)

        elif self.get(self.contains(dato)) == self.first or self.is_emtpy():
            self.add_first(dato_after)

        else:
            nuevo = DoublyLinkedListItem(dato_after)
            current_busqueda: DoublyLinkedListItem = self.first
            aux: DoublyLinkedListItem = None
            indice_dato = self.contains(dato)
            if indice_dato != -1:
                aux = self.get(indice_dato)
                current: DoublyLinkedListItem = aux.get_next()
                aux.set_next(nuevo)
                nuevo.set_next(current)
                nuevo.set_previous(aux)
                current.set_previous(nuevo)
                self.cant += 1

    def add_before(self, dato: int, dato_before: object) -> None:
        if self.get(self.contains(dato)) == self.last:
            self.add_last(dato_before)

        elif self.get(self.contains(dato)) == self.first or self.is_emtpy():
            self.add_first(dato_before)

        else:
            nuevo = DoublyLinkedListItem(dato_before)
            current_busqueda: DoublyLinkedListItem = self.first
            aux: DoublyLinkedListItem = None
            indice_dato = self.contains(dato)
            if indice_dato != -1:
                aux = self.get(indice_dato)
                current: DoublyLinkedListItem = aux.get_previous()
                current.set_next(nuevo)
                nuevo.set_previous(current)
                nuevo.set_next(aux)
                aux.set_previous(nuevo)
                self.cant += 1

    def clear(self) -> bool:
        if not self.is_emtpy():
            self.first = None
            self.last = None
            self.cant = 0
            return True
        else:
            return False

    def contains(self, dato: object) -> int:
        current: DoublyLinkedListItem = self.first
        existe: bool = False
        indice: int = 0
        while True:
            if current.get_dato() == dato:
                existe = True
                break
            indice += 1
            current = current.get_next()
            if current.get_next() == self.first.get_next():
                break
        if existe:
            return indice
        else:
            return -1

    def get(self, i: int) -> DoublyLinkedListItem:
        if i < 0 or i >= self.cant:
            return None

        current: DoublyLinkedListItem = self.first
        while True:
            if i == 0:
                return current
            i -= 1
            current = current.get_next()
            if current.get_next() == self.first.get_next():
                break
        return None

    def size(self) -> int:
        return self.cant

    def remove(self, dato: object) -> bool:
        current: DoublyLinkedListItem = self.first
        eliminar: DoublyLinkedListItem = None
        if self.first.get_dato() == dato:
            self.last.set_next(self.first.get_next())
            self.first.get_next().set_previous(self.last)
            self.first = self.first.get_next()
            self.cant -= 1
            return True

        if self.last.get_dato() == dato:
            current_l: DoublyLinkedListItem = self.last.get_previous()
            self.first.set_previous(current_l)
            current_l.set_next(self.first)
            self.last = current_l
            self.cant -= 1
            return True

        eliminar = self.get(self.contains(dato))
        if eliminar is not None:
            current_p: DoublyLinkedListItem = eliminar.get_previous()
            current_n: DoublyLinkedListItem = eliminar.get_next()
            current_p.set_next(current_n)
            current_n.set_previous(current_p)
            self.cant -= 1
            return True
        else:
            return False

    def remove_first(self) -> bool:
        if not self.is_emtpy():
            self.last.set_next(self.first.get_next())
            self.first.get_next().set_previous(self.last)
            self.first = self.first.get_next()
            self.cant -= 1
            return True
        else:
            return False

    def remove_last(self) -> bool:
        if not self.is_emtpy():
            current_l: DoublyLinkedListItem = self.last.get_previous()
            self.first.set_previous(current_l)
            current_l.set_next(self.first)
            self.last = current_l
            self.cant -= 1
            return True
        else:
            return False

    def __str__(self) -> str:
        salida: str = "["
        current: DoublyLinkedListItem = self.first
        if self.first is not None:
            while True:
                """
                if current.get_next() == self.first:
                    salida += str(current.get_dato())
                else:
                    salida += str(current.get_dato()) + ", "
                """
                salida += str(current.get_dato()
                              ) if current.get_next() == self.first else str(current.get_dato()) + ", "
                current = current.get_next()
                if current.get_next() == self.first.get_next():
                    break
        salida += "]"
        return salida

    def is_emtpy(self) -> bool:
        return self.cant == 0

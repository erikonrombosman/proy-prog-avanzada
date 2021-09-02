from doublylinkedlistitem.DoublyLinkedListItem import DoublyLinkedListItem


class DoublyLinkedList:
    first: DoublyLinkedListItem
    last: DoublyLinkedListItem
    cant: int

    def __init__(self) -> None:
        """ Create an intance of DoublyLinkedList
        """
        self.cant = 0
        self.last = None
        self.first = None

    def add_first(self, dato: object) -> None:
        """ Insert the first element in the list

        Args:
            dato: object to insert
        """
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
        """ Insert the last element in the list

        Args:
            dato: object to insert
        """
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
        """ Insert an element in the list after the given dato

        Args:
            dato: given dato
            dato_after: object to insert
        """
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
        """ Insert an element in the list before the given dato

        Args:
            dato: given dato
            dato_after: object to insert
        """
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
        """ Remove all items from the list

        Return:
            True if all items were removed
        """
        if not self.is_emtpy():
            self.first = None
            self.last = None
            self.cant = 0
            return True
        else:
            return False

    def contains(self, dato: object) -> int:
        """ Verifies if the entered data exists in the list

        Args:
            dato: object to check

        Return:
            Index of the element in the list or -1 if it doesn't exist
        """

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
        """ Returns an element corresponding to the indicated index 

        Args:
            i: int index of the item

        Return:
            DoublyLinkedListItem type element corresponding to the indicated index
        """

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
        """ Returns the size of the list

        Return:
            Size of the list 
        """

        return self.cant

    def remove(self, dato: object) -> bool:
        """ Removes an item from the list according to the data entered

        Args:
            dato: object to remove from the list

        Return:
            returns true if the item was removed 
        """

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
        """ Removes the first item from the list

        Return:    
            True if the item was removed 
        """

        if not self.is_emtpy():
            self.last.set_next(self.first.get_next())
            self.first.get_next().set_previous(self.last)
            self.first = self.first.get_next()
            self.cant -= 1
            return True
        else:
            return False

    def remove_last(self) -> bool:
        """ Removes the last item from the list

        Return:
            True if the item was removed 
        """
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
        """ Convert list elements to string 

        Return:
            The elements of the list as a string 
        """
        salida: str = "["
        current: DoublyLinkedListItem = self.first
        if self.first is not None:
            while True:

                salida += str(current.get_dato()
                              ) if current.get_next() == self.first else str(current.get_dato()) + ", "
                current = current.get_next()
                if current.get_next() == self.first.get_next():
                    break

        salida += "]"
        return salida

    def is_emtpy(self) -> bool:
        """ Check that the list is empty 

        Return:
            True if the number of elements in the list is 0 
        """
        return self.cant == 0

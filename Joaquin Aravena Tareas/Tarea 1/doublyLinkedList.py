from doublyLinkedListItem import DoublyLinkedListItem


class DoublyLinkedList:

    def __init__(self) -> None:
        self.first_item = None
        self.last_item = None

    def add_first(self, item: object) -> None:
        nuevo = DoublyLinkedListItem(item)
        # Lista vacía
        if self.first_item is None:
            self.first_item = nuevo
            self.last_item = nuevo
        else:
            self.first_item.set_previous(nuevo)
            nuevo.set_next(self.first_item)
            self.first_item = nuevo

    def add_last(self, item: object) -> None:
        nuevo = DoublyLinkedListItem(item)
        # Lista vacía
        if self.first_item is None:
            self.first_item = nuevo
            self.last_item = nuevo
        else:
            self.last_item.set_next(nuevo)
            nuevo.set_previous(self.last_item)
            self.last_item = nuevo

    def add_after(self, key: object, item: object) -> None:
        nuevo = DoublyLinkedListItem(item)
        current = self.first_item
        while current is not None:
            if current.get_dato() == key:
                nuevo.set_next(current.get_next())
                current.get_next().set_previous(nuevo)
                nuevo.set_previous(current)
                current.set_next(nuevo)
                break
            current = current.get_next()

    def add_before(self, key: object, item: object) -> None:
        nuevo = DoublyLinkedListItem(item)
        current = self.first_item
        while current is not None:
            if current.get_dato() == key:
                nuevo.set_previous(current.get_previous())
                current.get_previous().set_next(nuevo)
                nuevo.set_next(current)
                current.set_previous(nuevo)
                break
            current = current.get_next()

    def clear(self) -> None:
        self.first_item = None
        self.last_item = None

    def contains(self, item: object) -> int:
        current = self.first_item
        index = 0
        while current is not None:
            if current.get_dato() == item:
                return index
            index += 1
            current = current.get_next()
        return -1

    def remove(self, item: object) -> None:
        current = self.first_item
        while current is not None:
            if current.get_dato() == item and current == self.first_item:
                self.remove_first()
                break
            if current.get_dato() == item and current == self.last_item:
                self.remove_last()
                break
            if current.get_dato() == item:
                current.get_previous().set_next(current.get_next())
                current.get_next().set_previous(current.get_previous())
                break
            current = current.get_next()

    def remove_first(self) -> None:
        if self.first_item is not None:
            self.first_item = self.first_item.get_next()
            self.first_item.set_previous(None)

    def remove_last(self) -> None:
        if self.last_item is not None:
            self.last_item = self.last_item.get_previous()
            self.last_item.set_next(None)

    def __str__(self) -> str:
        current: DoublyLinkedListItem = self.first_item
        if self.first_item is None:
            return "[]"
        lista = "["
        while current is not None:
            if current != self.last_item:
                lista += str(current.get_dato()) + ", "
            else:
                lista += str(current.get_dato()) + "]"
            current = current.get_next()
        return lista

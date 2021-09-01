
class DoublyLinkedListItem:
    dato: object = None

    def __init__(self, dato: object) -> None:
        self.dato = dato
        self.previous = None
        self.nexts = None

    def get_dato(self) -> object:
        return self.dato

    def get_next(self):
        return self.nexts

    def get_previous(self):
        return self.previous

    def set_next(self, nodo):
        self.nexts = nodo

    def set_previous(self, nodo):
        self.previous = nodo

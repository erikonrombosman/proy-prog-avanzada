class DoublyLinkedListItem:

    def __init__(self, dato: object, next=None, previous=None) -> None:
        self.dato = dato
        self.next = next
        self.previous = previous

    def get_dato(self) -> object:
        return self.dato

    def set_next(self, next) -> None:
        self.next = next

    def get_next(self):
        return self.next

    def set_previous(self, previous) -> None:
        self.previous = previous

    def get_previous(self):
        return self.previous

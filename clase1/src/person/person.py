"""Person class."""

from dog.dog import Dog
class Person:

    def __init__(self, name: str, age: float, dogs: list[str]) -> None:
        """Creates an instance of person

        Args:
            name: String Person name
            age: float person age
            dogs: list[str]
        """
        self.name = name
        self.age = age
        aux_dogs = []
        for dog in dogs:
            aux_dogs.append(Dog(dog, self.name))
        self.dogs = aux_dogs
        

    def say_hi(self):
        """ Says hi to everyone
        """
        print('Hola a todos!')


    def talk_about_your_dogs(self):
        """say all your dogs name
        """
        word = f"My name is {self.name} and my dogs are: "
        for dog in self.dogs:
            word += f"{dog.name} "
        word += 'y los quiero mucho'
        print(word)
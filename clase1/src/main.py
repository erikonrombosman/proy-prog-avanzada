## Primer person se refiere al directorio person. El segundo person, al archivo person.py.
##  Desde ahí (por eso el from), importaremos la clase Person
from person.person import Person

if __name__ == "__main__":
    erik = Person('erik', 25, ['balto', 'leia'])
    erik.say_hi()
    erik.talk_about_your_dogs()
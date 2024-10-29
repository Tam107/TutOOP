class Animal:
    def __init__(self, name: str):
        self.__name = name

    def __str__(self):
        return f'Animal[{self.__name}]'

class Mammal(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def __str__(self):
        return f'Mammal[{Animal.__str__(self)}]'

class Dog(Mammal):
    def __init__(self, name: str):
        super().__init__(name)

    def greets(self, another = None):
        if another is None:
            print("Woof")
        else:
            print("Woooof")
    def __str__(self):
        return f'Dog[{Mammal.__str__(self)}]'

class Cat(Mammal):
    def __init__(self, name: str):
        super().__init__(name)

    def greets(self):
        print("Meow")

    def __str__(self):
        return f'Cat[{Mammal.__str__(self)}]'


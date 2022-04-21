from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes


    #Constructors
    def __init__(self):
        self.value = "Animal"


    #Methods
    @abstractmethod
    def reproduce(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def sleep(self):
        print("I am sleeping")

    def type(self):
        print(self.value)

class Mammal(Animal):
    #Attributes


    #Constructors
    def __init__(self):
        self.value = "Mammal"


    #Methods
    @abstractmethod
    def eat(self):
        pass
    
    def reproduce(self):
        print("Live Birth")

    def sleep(self):
        print("I am sleeping now")

    def type(self):
        print(self.value)

class Cat(Mammal):
     #Attributes


    #Constructors
    def __init__(self):
        self.value = "Cat"


    #Methods
    def type(self):
        print(self.value)

    def eat(self):
        print("I eat mice")

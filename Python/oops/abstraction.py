from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass

class Cat(Animal):
    def voice(self):
        print('meow-meow')

class Dog(Animal):
    def voice(self):
        print('bhow-bhow')


ob1 = Cat()
ob1.voice()
ob2 = Dog()
ob2.voice()





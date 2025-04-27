class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def get_breed(self):
        return self.breed

dog = Dog("Buddy", "Golden Retriever")
print(dog.get_name())  # Output: Buddy
print(dog.get_breed())  # Output: Golden Retriever

class Animal:
    def speak(self):
        print("I dunno what to say")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Dog(Animal):
    def speak(self):
        print("Woof")

cat = Cat()
dog = Dog()
cat.speak()  # Output: Meow
dog.speak()  # Output: Woof

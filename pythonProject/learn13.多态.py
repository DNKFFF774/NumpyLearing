#多态
class Animal:
    def speak(self):
        pass
#让父类来确定具体有什么方法，具体的实现由子类自行决定
class Dog(Animal):
    def speak(self):
        print("wolf")

class Cat(Animal):
    def speak(self):
        print("meow")

def make_noise(animal:Animal):
    animal.speak()

dog1=Dog()
cat1=Cat()
make_noise(dog1)
make_noise(cat1)
#多态含义：父类声明，子类工作，同一行为，不同状态

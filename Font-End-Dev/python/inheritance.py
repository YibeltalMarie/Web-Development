
# About inheritance 
# DRY = Don't Repeat Yourself

class Animal:
  def __init__(self):
    self.value = "Animal"

  def eat(self):
    print("eat")

class Mammal(Animal):
  def walk(self):
    print("walk")

class Fish(Animal):

  def swim(self):
    print("swim")

m = Mammal()
print(m.value)
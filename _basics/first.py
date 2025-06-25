class Animal:
  def breathe(self):
    print("breathing")
class Fish(Animal):
  def swim(self):
    super().breathe()
    print("dance")
fish=Fish()
#fish.breathe()
fish.swim()
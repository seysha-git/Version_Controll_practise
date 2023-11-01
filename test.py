#primary branch

#my new feature branch
print("my feature branch")

class Shield:
    def __init__(self, health):
        self.health = health
    def add(self, added):
        self.health += added

shield = Shield(100)

shield.add(20)

print(shield.health)



class Person:
    pass

class House:
    pass
        
class Animal:
    def __init__(self,name):
        self.name = name 

class Mammal(Animal):
    def __init__(self,name,animal_type):
        self.animal_type = animal_type

class Reptile(Animal):
    def __init__(self,name,animal_type):
        self.animal_type = animal_type    

stella = Reptile("Stella","alligator")
daisy = Mammal("Daisy","dog")

print(stella)
print(daisy)
class Vertebrate:
    ## this will be true for all 
    ## inherited class
    spinal_cord = True 

    def __init__(self,name):
        self.name = name 

class Mammal(Vertebrate):
    def __init__(self,name,animal_type):
        self.animal_type = animal_type 
        self.temperature_regulation = True


class Reptile(Vertebrate):
    def __init__(self,name,animal_type):
        self.animal_type = animal_type
        self.temperature_regulation = False

daisy = Mammal('Daisy','dog')
stella = Reptile("Stella",'alligator')

# Print stella's attributes spinal_cord and temperature_regulation
print("Stella Spinal cord: " + str(stella.spinal_cord))
print("Stella temperature regulation: " + str(stella.temperature_regulation))

# Print daisy's attributes spinal_cord and temperature_regulation
print("Daisy Spinal cord: " + str(daisy.spinal_cord))
print("Daisy temperature regulation: " + str(daisy.temperature_regulation))
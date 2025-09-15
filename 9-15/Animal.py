class Animal:
    def __init__(self, species, energy):
        self.species = species
        self.energy = energy
    
    def __str__(self):
        return f"{self.species} with energy {self.energy}"
    
    def play(self, energy_spent):
        self.energy -= energy_spent

    def rest(self, energy_recovered):
        self.energy += energy_recovered

class Lion(Animal):
    def __init__(self, species, energy, mane_length, roar):
        super().__init__(species, energy)
        self.mane_length = mane_length
        self.roar = roar

    def get_roar(self):
        return self.roar
    
king_lion = Lion("Lion", 100, 24, "GRRRRR")
cowardly_lion = Lion("Lion", 75, 12, "grrrrr")

print(king_lion)
print(king_lion.get_roar())
print(cowardly_lion)
print(cowardly_lion.get_roar())
class Reptil:
    def __init__(self, name, species, legs, toxicity):
        self.name = name
        self.species = species
        self.legs = legs
        self.toxicity = toxicity

    def jump(self, height):
        print(f"{self.name} can jump {height}.")

    def bite(self):
        if self.toxicity == 0:
            print(f"{self.name} can bite. Fortunately it is not poisonous.")
        else:
            print(f"{self.name} can bite. Careful, it is poisonous.")

    def __eq__(self, other):
        li = []
        comparison_name = bool(self.name == other.name)
        comparison_species = bool(self.species == other.species)
        comparison_legs = bool(self.legs == other.legs)
        comparison_toxicity = bool(self.toxicity == other.toxicity)
        if comparison_name == 1:
            li.append("Name")
        if comparison_species == 1:
            li.append("Species")
        if comparison_legs == 1:
            li.append("Legs")
        if comparison_toxicity == 1:
            li.append("Toxicity")
        if comparison_name + comparison_species + comparison_legs + comparison_toxicity == 4:
            return print("The objects with the names", other.name, "and", self.other, "are completely identical.")
        if comparison_name + comparison_species + comparison_legs + comparison_toxicity == 3:
            return print("The objects", self.name, "and", other.name, "are identical in 3 out of 4 properties:", li)
        if comparison_name + comparison_species + comparison_legs + comparison_toxicity == 2:
            return print("The objects", self.name, "and", other.name, "are identical in 2 out of 4 properties:", li)
        if comparison_name + comparison_species + comparison_legs + comparison_toxicity == 1:
            return print("The objects", self.name, "and", other.name, "are identical in 1 out of 4 properties:", li)
        return print("The objects", self.name, "and", other.name, "are completely different.")

    def __gt__(self, other):
        if self.legs > other.legs:
            return print("Object", self.name, "has more legs than", other.name)
        if self.legs < other.legs:
            return print("Object", self.name, "has less legs than", other.name)
        else:
            return print("Objects", self.name, other.name, "have the same amount of legs")


snake1 = Reptil("Hss", "snake", 0, 5)
snake1.bite()

snake2 = Reptil("Hsstwo", "snake", 0, 0)
snake2.bite()

lizard = Reptil("Shlurp", "Bearded Dragon", 4, 0)
print(snake1.name, snake1.species, snake1.legs, snake1.toxicity)

snake1 == snake2
snake2 == lizard
snake1 == lizard

snake1 > lizard

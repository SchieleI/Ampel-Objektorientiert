class Haustier:
    def __init__(self, name, futter, spielzeug):
        print(self)
        self.name_attribut1 = name
        self.futter_attribut2 = futter
        self.spielzeug_attribut3 = spielzeug

    def fuettern(self):
        return ("Das Tier wird gefÃ¼ttert.")

    def gassigehen(self):
        return (f"Der Hund{self.name_attribut1} geht Gassi.")


haustier_objekt1 = Haustier("Kurt", "Pizza", "Ball")

print(type(haustier_objekt1))
print(haustier_objekt1.name_attribut1)
print(haustier_objekt1.futter_attribut2)
print(haustier_objekt1.spielzeug_attribut3)

haustier_objekt1.name_attribut1 = "Neuer Name"

haustier_objekt2 = Haustier("Fritz", "nix", "Socken")

print(haustier_objekt2.spielzeug_attribut3)
print(haustier_objekt2.fuettern())
print(haustier_objekt1.gassigehen())
print(haustier_objekt2.gassigehen())
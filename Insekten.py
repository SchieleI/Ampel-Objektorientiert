class Insekt:
    def __init__(self, anzahl_augen, giftlevel, geschwindigkeit, name):
        self.eye = anzahl_augen
        self.poison = giftlevel
        self.speed = geschwindigkeit
        self.name = name
    def springen(self, hoehe):
        print(f"{self.name} springt {hoehe} hoch.")
    def fliegen(self):
        print(f"{self.name} kann fliegen.")
    def stechen(self):
        print(f"{self.name} kann stechen.")
    def __eq__(self, other):
        return (self.name == other.name) or (self.eye == other.eye)

class Reptil:
    def __init__(self, typ, anzahl_beine, name):
        self.type = typ
        self.leg = anzahl_beine
        self.name = name
    def kriechen(self, strecke):
        print(f"{self.name}")
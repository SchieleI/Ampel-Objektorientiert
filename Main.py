from tiere import Insekt
from tiere import Reptil



biene = Insekt(2, 5, 10, "Willi")
fliege = Insekt(50, 0, 8, "Peter")

biene.springen("10 cm")
fliege.springen("7 cm")
biene.fliegen()
biene.stechen()
biene.name = "Maaaaaaaaaaja"
biene.fliegen()

biene2 = Insekt(2, 27, 10, "Willi")

# Der == Operator ist überladen

if 5 == 5:
    print("Die beiden Zahlen sind gleich.")

if biene.speed == biene2.speed:
    print("Der Speed ist gleich.")

if biene == biene2:
    print("Das ist die gleiche Biene.")

krokodil = Reptil("böse", "4", "Manni")
print(krokodil.name)
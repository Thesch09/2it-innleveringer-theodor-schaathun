# Ingen AI/KI er brukt av meg, Theodor Schaathun
# Oppgave: Lister
import random
# eksempel: listMcList = ["Bob", "Janet", "Mistilteinn, Tree Crown without a Ruler", "John"]
planeter = ["Jorda", "Popstar", "Eris", "PNF 404", "Deep-Dish 9", "Planet X"]
for planet in planeter:
    print(planet)
print()
planeter.sort()
for planet in planeter:
    print(planet)
print()
planeter.append("The Cookie Planet")
for planet in planeter:
    print(planet)
print()
planeter.insert(int(len(planeter)/2),"New World")
for planet in planeter:
    print(planet)
print()
planeter[2] = "Terra"
for planet in planeter:
    print(planet)
print()
planeter.remove("Terra")
for planet in planeter:
    print(planet)

print()
if "Popstar" in planeter:
    print("Popstar eksisterer")

print()
spaces = ""
for p in planeter[random.randint(0,len(planeter)-1)]:
    print(f"{spaces}{p}")
    spaces += " "

# tuples
# example: thisTuple = (0,124)
bob = (0,533)
print(bob)
bob = (58, bob[1])
print(bob[0])
for bobNumber in bob:
    print(bobNumber**2)

for index, planet in enumerate(planeter):
    print(index, planet)

# sets
# example: thisSet = {0,0}
# Null LLM basert AI/KI blir brukt av Theodor Schaathun
from rich import print

planets = ["Popstar", "New World", "The Planet that is slowly Cracking and Crumbling and Shattering and will soon be Lost, girl", "PNF 404", "Not Neptune"]
print(planets)
print(planets[0])
print(planets[-1])
print(len(planets))
planets.append("Neptune")
print(planets)
print(planets[0])
print(planets[-1])
print(len(planets))

planets.remove("Neptune")
shatteredPlanet = planets.pop(2)
print(f"Whoops! It looks like \"{shatteredPlanet}\" cracked, crumbled and shattered, and therefore is lost")
if shatteredPlanet != "The Planet that is slowly Cracking and Crumbling and Shattering and will soon be Lost, girl":
    print("\tWhat do you mean that \"The Planet that is slowly Cracking and Crumbling and Shattering and will soon be Lost, girl\" wasn't the one to crack, crumble and shatter, and is therefore not lost???")
else:
    print("\tWho would've guessed that \"The Planet that is slowly Cracking and Crumbling and Shattering and will soon be Lost, girl\" cracked, crumbled and shattered, and is therefore lost?")
print(planets)
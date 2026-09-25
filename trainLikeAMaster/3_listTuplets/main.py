# Null LLM basert AI/KI blir brukt av Theodor Schaathun
from rich import print
import random

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

expedition = []
print("Brave cadet! How many planets will you visit on your maiden voyage?")
try:
    for expeditionLength in range(int(input())):
        print("Which planets would you like to visit. Give them to me one at a time")
        planet = input()
        for planety in planets:
            if planet.lower() == planety.lower():
                break
        else:
            print("You can look for it, but it might not be a success")
            if random.randint(1,len(planet)) != 1:
                planet = "[red]Failed Expedition"
        expedition.append(planet)
    print()
    input("Press ENTER to continue")
    for index, exped in enumerate(expedition):
        print(index+1, exped)
        for planety in planets:
            if exped.lower() == planety.lower():
                break
        else:
            if exped != "[red]Failed Expedition":
                print("\tNew planet! Adding to list")
                planets.append(exped)
    failureToConnectUnderTheInfluence = False

except ValueError:
    failureToConnectUnderTheInfluence = True # refrence to a MSN prompt
    print("We had brave hopes for you cadet, but as you either didn't write a number or included even a single decimal point, we'll have to fire you. If you wish to retry, you will be able to restart the 7 year course in 48 years when your ban lifts")
    print("You should've known that it would get you fired and banned for 48 years")

if not failureToConnectUnderTheInfluence:
    print("cont")
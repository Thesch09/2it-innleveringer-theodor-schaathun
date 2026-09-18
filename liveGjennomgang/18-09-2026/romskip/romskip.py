# get ready for a game changereeno
# Null AI/KI er brukt i denne oppgaven av meg, Theodor Schaathun

def openFile(file):
    with open(file, "r") as fil:
        drivstoff = int(fil.read())
    return drivstoff

def checkFuel(fuel):
    print(f"Drivstoff: {fuel}%")
    if fuel >= 50:
        return "Du har nok drivstoff for å komme deg hjem"
    else:
        return "Du trenger mer drivstoff for å komme deg hjem"

drivstoff = openFile("drivstoff.txt")
print(checkFuel(drivstoff))

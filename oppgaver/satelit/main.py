# Null AI/KI

satellites = []
class satellite:
    def __init__(self, name, planet, distEarth):
        self.name = name
        self.planet = planet
        self.distEarth = distEarth
        satellites.append(self)

    def sendMessage(self):
        lines = ""
        lengthName = len(f"Navn: {self.name}")
        lengthPlanet = len(f"Planet: {self.planet}")
        if lengthName > lengthPlanet:
            for i in range(lengthName):
                lines += "-"
        else:
            for i in range(lengthPlanet):
                lines += "-"
        print(lines)
        print(f"Navn: {self.name}")
        print(f"Planet: {self.planet}")
        print(lines)

satlit = satellite("Mickey","Pluto", 4500000000)
satlit = satellite("The Flush Five", "Eris",14410000000)
satlit = satellite("Lil' Jimmy", "Sola", 149600000)
for satelliteThing in satellites:
    satelliteThing.sendMessage()
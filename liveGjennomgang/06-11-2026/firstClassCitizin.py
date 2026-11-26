folk = []
class Person:
    def __init__(self, navn, alder, hoyde, yrke = "har ikke jobb"):
        self.navn = navn
        self.alder = alder
        self.hoyde = hoyde
        self.yrke = yrke
        folk.append(self)

    def hvemErJeg(self):
        print(f"Jeg heter {self.navn}. Jeg er {self.alder} år gammel. Jeg er {self.hoyde}cm høy.")
        if self.yrke != "har ikke jobb":
            print(f"Jeg jobber som {self.yrke}")
        else:
            print("Jeg har ikke jobb")
        print()

    def becomeOld(self):
        print(f"Jeg, {self.navn}, har blitt eldre. Jeg var {self.alder} og nå er {self.alder+1}år gammel\n")
        self.alder += 1

    def jobb(self):
        print(f"{self.navn} jobber")

class Laerer(Person):
    def rettOpg(self):
        print(f"{self.navn} rettet en oppgave")

    def jobb(self):
        print(f"Læreren {self.navn} jobber")

class UnemployedLoserLookAtThisAbsoluteLoser(Person):
    def __init__(self, navn, alder, hoyde):
        super().__init__(navn, alder, hoyde)
        self.loseSteak = 0

    def lose(self):
        print(f"{self.navn} just\nl  | lI\nll | l-\nthe game")
        self.loseSteak += 1
        print(self.loseSteak)
        print()

    def jobb(self):
        print(f"{self.navn} har ikke en jobb, så {self.navn} sier bare Bee Movie Scriptet")
        print("According to all known laws of aviation, there is no way a bee should be able to fly.\nIts wings are too small to get its fat little body off the ground.\nThe bee, of course, flies anyway because bees don't care what humans think is impossible.\nYellow, black. Yellow, black. Yellow, black. Yellow, black.\nOoh, black and yellow!\nLet's shake it up a little.\nBarry! Breakfast is ready!\nComing!")
    

ola = Person("Ola", 35, 150, "snekker")
kari = Person("Kari", 77, 170, "besta")
filip = Person("Filip", 6, 1)
jacob = Laerer("Jacob", 27, 10, "2IT")
losalot = UnemployedLoserLookAtThisAbsoluteLoser("John Losalot", 10, 180)

filip.hvemErJeg()
filip.becomeOld()
jacob.rettOpg()
losalot.lose()

for person in folk:
    print()
    person.hvemErJeg()
    person.jobb()
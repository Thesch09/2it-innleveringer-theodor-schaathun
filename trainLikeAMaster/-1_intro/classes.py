class fighter:
    def __init__(self):
        print("Make! A! FIGHERRRRR!!!!!")
        self.firstName = input("What is the first name of [UNAMED FIGHTER]?\n")
        self.sirName = input(f"What is the surname of {self.firstName}?\n")
        self.nickyName = input(f"Does {self.firstName} {self.sirName} have a nickname? Leave empty for none. \n")
        if self.nickyName == "":
            questionaryName = f"{self.firstName} {self.sirName}"
        else:
            questionaryName = f"{self.nickyName}"
        while True:
            try:
                self.maxHp = int(input(f"How old is {questionaryName}? This will have consequences.\n"))
                break
            except ValueError:
                print("That's not a number! Try again")
        
        while True:
            try:
                self.maxHp = int(input(f"How much max HP does {questionaryName} have?\n"))
                break
            except ValueError:
                print("That's not a number! Try again")
        self.hp = self.maxHp
        while True:
            try:
                self.regen = int(input(f"How fast does {questionaryName} regen (%)? This will have consequences.\n"))
                if self.regen > 100:
                    print("That's more than one hundred, pick a smaller number")
                elif self.regen < 0:
                    print("That's less than zero, pick a larger number")
                elif self.regen == 0:
                    if input(f"This will make {questionaryName} a glass cannon as they'll be unable to heal. Type Y if you want them to be a glass cannon").lower() == "y":
                        break
                else:
                    break
            except ValueError:
                print("That's not a number! Try again")
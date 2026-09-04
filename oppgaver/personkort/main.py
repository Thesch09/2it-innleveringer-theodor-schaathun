from rich import print
import os

def langSetup():
    global lang
    langUndefined = True
    while langUndefined:
        os.system("cls")
        print("Språk/Language")
        print("EN = English\nNO = Norsk")
        lang = input().lower()
        print()
        if lang == "en":
            print("Language set to English")
            langUndefined = False
        elif lang == "no":
            print("Språk er satt til Norsk")
            langUndefined = False
        else:
            print("Null språk funnet\nNo language detected")
        input("Trykk på ENTER for å fortsette\nPress ENTER to continue\n")

def addAGuy(source):
    global lang
    global guys
    if source == "noob":
        if lang == "en":
            name = input("What is your name?\n")
            while True:
                age = input("How old are you?\n")
                try:
                    age = int(age)
                    break
                except ValueError:
                    print("That's Not a Number")
            while True:
                height = input("How tall are you?\n")
                try:
                    height = int(height)
                    break
                except ValueError:
                    print("That's Not a Number")
            while True:
                oohYoureACodeLiker = input("Do you like programming? y/n\n").lower()
                if oohYoureACodeLiker == "y" or oohYoureACodeLiker == "n":
                    break
                else:
                    print("That's not y/n...")
            funielFactiel = input("And finally, give me a fun fact of yours. Hand it over :gun:")
        if lang == "no":
            name = input("Hva heter du?\n")
            while True:
                age = input("Hvor gammel er du?\n")
                try:
                    age = int(age)
                    break
                except ValueError:
                    print("Det er Ikke et Tall")
            height = input("Hvor høy er du?\n")
            while True:
                oohYoureACodeLiker = input("Liker du programmering?? y/n\n").lower()
                if oohYoureACodeLiker == "y" or oohYoureACodeLiker == "n":
                    break
                else:
                    print("Det er ikke y/n...")
            funielFactiel = input("Og til slutt, gi meg en fun fact om deg. Gi den til meg :gun:")
        if oohYoureACodeLiker == "y":
            oohYoureACodeLiker = True
        else:
            oohYoureACodeLiker = False
        guys.update({name:[age,height,oohYoureACodeLiker,funielFactiel]})

guys = {}

langSetup()
while True:
    os.system("cls")
    if lang == "en":
        print("Welcome!")
        print("What do you want to do?")
        print("1. Add a new person")
        print("2. Look at people")
        print("3. Change language")
        print("4. End")
    elif lang == "no":
        print("Velkommen!")
        print("Hva vil du gjøre?")
        print("1. Legge til en ny person")
        print("2. Se på folk")
        print("3. Endre språk")
        print("4. Slutte")
    inputio = input()
    print()
    try:
        inputio = int(inputio)
    except ValueError:
        if lang == "en":
            print("That is not a number")
        elif lang == "no":
            print("Det er ikke et tall")
    if inputio == 4:
        if lang == "en":
            print("GOODBYE!!!")
        elif lang == "no":
            print("HA DET!!!")
        break
    elif inputio == 3:
        langSetup()
    elif inputio == 1:
        addAGuy("noob")
    elif inputio == 2:
        for guy in guys:
            if lang == "en":
                print(f"Name: {guy}")
                print(f"Age: {guys[guy][0]}")
                print(f"Height: {guys[guy][1]}")
                if guys[guy][2]:
                    print("Likes programming")
                else:
                    print("HATES programming. Nr. 1 programming HATER")
                print(f"Fun Fact: {guys[guy][3]}")
                print("\nWhat will you do next?")
                print("1. Stop")
                print("2. Kill (delete)")
                print("Everything else, next guy")
            elif lang == "no":
                print(f"Navn: {guy}")
                print(f"Alder: {guys[guy][0]}")
                print(f"Høyde: {guys[guy][1]}")
                if guys[guy][2]:
                    print("Liker programmering")
                else:
                    print("HATER programmering. Nr. 1 programmering HATER")
                print(f"Fun Fact: {guys[guy][3]}")
                print("\nHva vil du gjøre?")
                print("1. Stoppe")
                print("2. Mord (slett)")
                print("Alt annet, neste person")
            
            inputio = input()
            if inputio == "1":
                break
            elif inputio == "2":
                guys.pop(guy)
                break
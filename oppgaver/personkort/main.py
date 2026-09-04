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
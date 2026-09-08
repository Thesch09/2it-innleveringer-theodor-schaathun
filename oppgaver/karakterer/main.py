from rich import print

validScore = False
while True:
    poeng = input("Hvor mange poeng fikk du på oppgaven?\n")
    try:
        poeng = int(poeng)
        if not poeng > 100 or not poeng < 0:
            print("Det er enten mer enn 100 eller mindre enn 0. Velg et tall imellom")
        else:
            validScore = True
    except:
        print("Det er ikke et tall. Vennligst skriv inn et tall")
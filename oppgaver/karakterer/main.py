from rich import print

while True:
    poeng = input("Hvor mange poeng fikk du på oppgaven?\n")
    try:
        poeng = int(poeng)
        if poeng > 100 or poeng < 0:
            print("Det er enten mer enn 100 eller mindre enn 0. Velg et tall imellom")
        else:
            if poeng < 50:
               print("Dessverre har du ikke bestått")
            elif poeng < 70:
                print("Du har bestått")
            elif poeng < 90:
                print("Du har gjort det ganske så bra")
            elif poeng >= 90:
                print("Du har gjort det VELDIG bra")
    except:
        print("Det er ikke et tall. Vennligst skriv inn et tall")
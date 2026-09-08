from rich import print

while True:
    poeng = input("Hvor mange poeng fikk du på oppgaven?\n")
    try:
        poeng = int(poeng)
        if poeng > 100 or poeng < 0:
            print("Det er enten mer enn 100 eller mindre enn 0. Velg et tall imellom")
        else:
            if poeng < 50:
                if poeng == 0:
                   print("Det var [red]VELDIG[/] dårlig. Hvordan?")
                else:
                    print("Dessverre har du [red]ikke bestått.")
            else:
                message = "Du har [green]bestått[/]"    
                if poeng < 70:
                    message += "."
                elif poeng < 90:
                    message += ", og du gjorde det godt."
                elif poeng < 100:
                    message += ", og du gjorde det VELDIG godt!"
                else:
                    message += ", og du gjorde det [red]P[orange3]E[yellow]R[green]F[blue]E[purple4]K[magenta]T[white]!"
                print(message)
    except:
        print("Det er ikke et tall. Vennligst skriv inn et tall")
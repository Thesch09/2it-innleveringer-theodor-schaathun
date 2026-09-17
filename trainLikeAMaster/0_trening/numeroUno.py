falsktNavn = "Ola"
print(falsktNavn)
print()

falskAlder = 9487100829417807103487589012
falskHoyde = 0.001 # teeny tiny
thyLoveOfPython = True
print(falsktNavn)
print(type(falsktNavn))
print(falskAlder)
print(type(falskAlder))
print(falskHoyde)
print(type(falskHoyde))
print(thyLoveOfPython)
print(type(thyLoveOfPython))

priceOfTheSoul = 69
antall = -9.99
total = priceOfTheSoul * antall
print(f"{priceOfTheSoul}*{antall}={total}")
priceOfTheSoul = 52
antall = 3
total = priceOfTheSoul * antall
print(f"{priceOfTheSoul}*{antall}={total}")

while True:
    try:
        applings = input("Tell me your applings, young one.\n")
        applings = int(applings)
        break
    except ValueError:
        print("Young one, that is not a number")
if applings < 0:
    print("You can't have negative applings")
elif applings <= 20:
    print("You have so few applings")
elif applings <= 1000:
    print("That's an adequate amount of applings")
else:
    print(f"OH GEEZ!!! {applings}??? {applings} IS TOO MANY APPLINGS. I'M SENDING YOU TO THE POLOICE")
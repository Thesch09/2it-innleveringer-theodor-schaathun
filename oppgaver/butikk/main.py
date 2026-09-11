from rich import print # fin terminal
import os
import time
import random
import webbrowser
import json

storeStock = {}
playerCart = {}
previousPurchases = {}
YTvideos = {}

with open(r"oppgaver/butikk/jsons/store.json") as jason:
    josh = json.loads(jason.read())
    storeStock = josh
with open(r"oppgaver/butikk/jsons/previousPurchase.json") as jason:
    josh = json.loads(jason.read())
    previousPurchases = josh
with open(r"oppgaver/butikk/jsons/youtube.json") as jason:
    josh = json.loads(jason.read())
    YTvideos = josh

def addPerson(playerCart):
    while True:
        os.system("cls")
        print("Før du drar, hva heter du?")
        name = input()
        if name in previousPurchases:
            print("Dessverre er det navnet allerede i systemet vært, vennligst velg et annet")
            input()
        else:
            previousPurchases.update({name:playerCart})
            with open(r"oppgaver/butikk/jsons/previousPurchase.json", "w") as jason:
                josh = json.dumps(previousPurchases)
                jason.write(josh)
            return
    
def buyThing(storeStock, playerCart):
    goodUnconfirmed = True
    while goodUnconfirmed:
        os.system("cls")
        print("Varer\n")
        for ware in storeStock:
            print(f"{ware}: {storeStock[ware]}kr")
        print("\nHva vil du kjøpe?")
        purchasable = input().lower().split(" ")
        newStr = ""
        for word in purchasable:
            word = word.capitalize()
            newStr += f"{word} "
        purchasable = newStr.strip()
        if purchasable in storeStock:
            while goodUnconfirmed:
                print("Hvor mange vil kjøpe?")
                amount = input()
                try:
                    amount = int(amount)
                    goodUnconfirmed = False
                    if purchasable in playerCart:
                        playerCart.update({purchasable:amount+playerCart[purchasable]})
                    else:
                        playerCart.update({purchasable:amount})
                    print(f"Kjøpte {amount} {purchasable}")
                except ValueError:
                    print("Det er ikke et helt tall, vennligst velg et helt tall")
                    input()
                    os.system("cls")

def lookAtCart(storeStock, playerCart):
    for item in playerCart:
        print(f"{playerCart[item]}x {item}: {storeStock[item]*playerCart[item]}kr")
    input()

def openYT(playerCart):
    print(f"Siden du kjøpte {playerCart["Youtube Video"]} videoer, så åpnes de videoene")
    YTurls = []
    YTtitles = []
    for video in YTvideos:
        YTurls.append(YTvideos[video])
        YTtitles.append(video)
    for video in range(playerCart["Youtube Video"]):
        whichVid = random.randint(0,len(YTvideos)-1)
        vid = YTurls[whichVid]
        webbrowser.open(f"https://www.youtube.com/watch?v={vid}", new=0, autoraise=True)
        print(f"Åpner {YTtitles[whichVid]}")
        time.sleep(random.randint(3,5))

def checkout(storeStock, playerCart):
    totPrice = 0
    for item in playerCart:
        print(f"{playerCart[item]}x {item}: {storeStock[item]*playerCart[item]}kr")
        totPrice += storeStock[item]*playerCart[item]
    print(f"Totalt: {totPrice}kr")
    print("Er du klar for å betale? Skriv JA hvis du er")
    checkyOut = input()
    if checkyOut.lower() == "ja":
        print("[red]Hacker PC...")
        time.sleep(random.randint(5,10)/10)
        print("[red]Hacket!")
        print("[red]Finner kortnummer")
        time.sleep(random.randint(5,10)/10)
        print("[red]Funnet!")
        print()
        print("Takk for at du har brukt Theo-butikken i dag!")
        print(f"{totPrice} kroner har blitt trukket fra kontoen din")
        input()
        if "Youtube Video" in playerCart:
            if playerCart["Youtube Video"] > 0:
                openYT(playerCart)
        return True

def lookAtPeople(pP, sS):
    if len(pP) < 1:
        os.system("cls")
        print("But nobody came.")
        input()
        os.system("cls")
        print("But nobody came.\nDet er en referanse til Undertale!")
        input()
        return
    else:
        for person in pP:
            os.system("cls")
            print(f"Navn: {person}")
            for item in pP[person]:
                if item in sS: # storeStock
                    print(f"{pP[person][item]}x {item}: {sS[item]*pP[person][item]}")
                else:
                    print(f"Ukjent vare: {pP[person][item]}x {item}")
            input()

while True:
    os.system("cls")
    print("Velkommen til Theo-butikken!!!")
    print("Hva vil du gjøre?")
    print("1. Kjøpe noe")
    print("2. Se handlekurven")
    print("3. Betale og DRA!!!")
    print("4. Se på forrige folk som har vært her")
    action = input()
    if action == "1":
        buyThing(storeStock, playerCart)
    elif action == "2":
        lookAtCart(storeStock, playerCart)
    elif action == "3":
        if checkout(storeStock, playerCart):
            addPerson(playerCart)
            break
    elif action == "4":
        lookAtPeople(previousPurchases,storeStock)
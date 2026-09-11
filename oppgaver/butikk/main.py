from rich import print # fin terminal
import os
import time
import random
import webbrowser
import json

storeStock = {}
playerCart = {}
youtubeVideos = {"Never Gonna Give You Up":"dQw4w9WgXcQ", "Let's Play ALL of Tears of the Kingdom":"3B21d32wn9s", "SCOTLAND FOREVER":"-BD1vHgYRgg", "xnopyt - Scott":"aMgCBYgVwsI", "xnopyt - Rin":"DV5HBcjw_8I", "Everything?":"CccHBlGrOu8", "Nuthing?":"BG7273yDpdA", "a complete history of the star trek franchise, 100% from memory, with no fact checking":"YyKyyDtLrSE"}

with open(r"oppgaver/butikk/jsons/store.json") as jason:
    josh = json.loads(jason.readline())
    storeStock = josh

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
    for video in range(playerCart["Youtube Video"]):
        YTurls = []
        YTtitles = []
        for video in youtubeVideos:
            YTurls.append(youtubeVideos[video])
            YTtitles.append(video)
        print(YTurls)
        whichVid = random.randint(0,len(youtubeVideos)-1)
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

while True:
    os.system("cls")
    print("Velkommen til Theo-butikken!!!")
    print("Hva vil du gjøre?")
    print("1. Kjøpe noe")
    print("2. Se handlekurven")
    print("3. Betale og DRA!!!")
    action = input()
    if action == "1":
        buyThing(storeStock, playerCart)
    elif action == "2":
        lookAtCart(storeStock, playerCart)
    elif action == "3":
        if checkout(storeStock, playerCart):
            with open(r"oppgaver/butikk/jsons/previousPurchase.json", "a") as jason:
                josh = json.dumps(playerCart)+"\n"
                jason.write(josh)
            break
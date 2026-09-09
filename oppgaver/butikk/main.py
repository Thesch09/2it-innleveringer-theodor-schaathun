from rich import print # fin terminal
import os

storeStock = {"Energi Drikk":25, "Baguette":45}
playerCart = {}

def buyThing(storeStock, playerCart):
    goodUnconfirmed = True
    while goodUnconfirmed:
        os.system("cls")
        print("Varer\n")
        for ware in storeStock:
            print(f"{ware}: {storeStock[ware]}")
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
        print(f"{playerCart[item]}x {item}: {storeStock[item]*playerCart[item]}")
    input()



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
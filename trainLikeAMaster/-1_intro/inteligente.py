
while True:
    try:
        answerToLife = input("What do you think the meaning of life is?\n")
        answerToLife = int(answerToLife)
        break
    except ValueError:
        if answerToLife.lower() == "pizza":
            print("Objectively correct")
            break
        print("try anew")

if answerToLife == 42:
    print("WOOWY ZOOWY HITCHHIKERS GUIDE TO LE GALAXY")
elif answerToLife != "pizza":
    print("LOUD INCORRECT BUZZER")
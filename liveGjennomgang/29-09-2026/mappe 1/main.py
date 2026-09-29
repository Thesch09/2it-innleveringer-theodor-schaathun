# Just like Daniel Failboat in the making of Cata-Bomb, I, Theodor Schaathun, use no AI
# Dictionary
import random

makeFunnyJokeAboutDictsHere = {
    "funnies":"joke",
    "even funnieser":"joke",
    "boringo":"What mi c e   i n   t h e   c a r p e t"
}
for entry in makeFunnyJokeAboutDictsHere:
    print(f"{entry}:{makeFunnyJokeAboutDictsHere[entry]}")
print(makeFunnyJokeAboutDictsHere)

fileContent = {} # It be happy with it's life
with open(r"liveGjennomgang/29-09-2026/mappe1/fil.txt", "r") as fil:
    #print(fil.read())
    print(type(fil))
    for line in fil:
        #print(type(line))

        line = str(line)
        lineSplit = line.split("\n")
        lineSplit = lineSplit[0].split(":")
        if len(lineSplit) == 2:
            print(lineSplit[0])
            try:
                lineVal = int(lineSplit[1])
                print("Value is an int")
            except ValueError:
                try:
                    lineVal = float(lineSplit[1])
                    print("Value is a float")
                except ValueError:
                    lineVal = lineSplit[1]
                    print("Value is a string")
            fileContent.update({lineSplit[0]:lineVal})
        else:
            print("Line either too long or not long enough")
print(fileContent)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","\t",". ", ", ", ":","end"]
with open(r"liveGjennomgang/29-09-2026/mappe1/otherFil.txt", "a") as fil:
    stringCheese = ""
    while True:
        letter = alphabet[random.randint(0,len(alphabet)-1)]
        if letter == "end" or len(stringCheese) > 50:
            break
        stringCheese += letter
    print(stringCheese)
    fil.write(f"{stringCheese}\n")

print("Please input a planetary object you'd like to visist")
planet = input()
print("And how many mooms?")
try:
    mooms = input()
    mooms = float(mooms)
    mooms = int(mooms)
except ValueError:
    mooms = ""
with open(r"liveGjennomgang/29-09-2026/mappe1/thirdFil.txt","w") as fil:
    fil.write(f"{planet}\n")
    if mooms != "":
        fil.write(f"\t{mooms} mooms\n")
    print(f"Saved {planet}")

print()
with open(r"liveGjennomgang/29-09-2026/mappe1/thirdFil.txt","r") as fil:
    for line in fil:
        print(line.split("\n")[0])
# Just like Daniel Failboat in the making of Cata-Bomb, I, Theodor Schaathun, use no AI
# Dictionary

makeFunnyJokeAboutDictsHere = {
    "funnies":"joke",
    "even funnieser":"joke",
    "boringo":"What mi c e   i n   t h e   c a r p e t"
}
for entry in makeFunnyJokeAboutDictsHere:
    print(f"{entry}:{makeFunnyJokeAboutDictsHere[entry]}")
print(makeFunnyJokeAboutDictsHere)

fileContent = {} # It be happy with it's life
with open(r"liveGjennomgang/29-09-2026/fil.txt", "r") as fil:
    #print(fil.read())
    print(type(fil))
    for line in fil:
        #print(type(line))

        line = str(line)
        lineSplit = line.split("\n")
        lineSplit = lineSplit[0].split(":")
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
print(fileContent)
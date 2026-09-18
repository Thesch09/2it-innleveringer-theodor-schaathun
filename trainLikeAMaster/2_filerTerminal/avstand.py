# No Al, nor AI/KI

def readDist(file):
    with open(file, "r") as phil:
        return float(phil.read().split("\n")[0])

def judgeDist(dist):
    print(f"Avstand: {dist:.2f}km")
    if dist < 10000:
        return "Du er nærme planeten"
    else:
        return "Du er langt unna planeten"

dist = readDist("avstand.txt")
print(judgeDist(dist))

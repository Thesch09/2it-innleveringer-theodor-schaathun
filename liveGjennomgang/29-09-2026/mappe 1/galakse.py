# Just like Daniel Failboat in the making of Cata-Bomb, I, Theodor Schaathun, use no AI
# files

try:
    with open(r"liveGjennomgang/29-09-2026/mappe1/galakse.txt", "r") as fil:
        print(fil.read())
except FileNotFoundError:
    print("Filen eksisterer ikke")

print("Velg planet nummer")
try:
    planetNummer = int(input())
except ValueError:
    print("Det er ikke et helt tall")
else:
    print("Tusen takk")
# Null AI/KI, jeg, Theodor Schaathun, bruker det ikke

def readTemp(file):
    with open(file, "r") as fil:
        return float(fil.read().split("\n")[0])

def judgeTemp(temp):
    print(f"Temperatur: {temp:.2f} grader")
    if temp < 0:
        return "Under frysepunktet"
    else:
        return "Over frysepunktet"

temp = readTemp("temperatur.txt")
print(judgeTemp(temp))

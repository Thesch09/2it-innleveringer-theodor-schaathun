# NULL AI/KI blir brukt av meg, Theodor Schaathun

def vurderOksygen(percent):
    print(f"Oksygen: {percent}%")
    if percent >= 50:
        return "Oksygennivå O"
    else:
        return "Lavt oksygennivå"
def readOxygen(file):
    with open(file,"r") as oks:
        return int(oks.read().split("\n")[0])
oxygen = readOxygen("oksygen.txt")
print(vurderOksygen(oxygen))

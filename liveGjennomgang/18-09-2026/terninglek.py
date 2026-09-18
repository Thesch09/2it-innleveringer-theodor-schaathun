# 0, bruk if
die = [6,5,5,2,1]
print()
if die[4]//(die[0]/die[3])/die[1]/die[2] == 0:
    print(die[4]//(die[0]/die[3])/die[1]/die[2])
    print("ya deed it")

# 1, bruk variable
die = [6,6,5,5,2]
math = die[1]/(die[0]/die[4])-die[2]/die[3]
print(math)

# 2, bruk if
die = [6,5,5,3,1]

math = die[0]/die[3]-die[1]/die[2]+die[4]
print(math)
if math == 2:
    print("ya deed it")

# 3, bruk funksjon
die = [4,3,1,1,1]
def doIt(d):
    print(d[1]//d[0]+d[2]+d[3]+d[4])
doIt(die)

# 4, bruk return
die = [4,2,1,1,1]
def doIt(d):
    return d[0]/d[1]+d[2]+d[3]*d[4]
print(doIt(die))

# 5, bruk variabel
die = [5,4,3,2,1]
math = die[0]-die[2]-die[3]+die[1]+die[4]
print(math)

# 6, bruk funksjon
die = [4,4,3,1,1]
def doIt(d):
    print(d[1]//d[0]+d[2]+d[3]+d[4])
doIt(die)
# 7, bruk funksjon
die = [6,6,6,6,2]
def doIt(d):
    print(d[0]/d[1]*d[2]+d[3]/d[4])
doIt(die)
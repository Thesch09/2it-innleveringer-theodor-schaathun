# I still don't understand why I'd even want to use AI for these tasks, they're far too easy. So no AI usage

def readWater(file): # The reason I've been putting file as an argument here is so that multiple different files can be used as sepperate points, for this task they could be water tanks
    with open(file, "r") as philza: # the with part causes 1) it gets indented and 2) it will automatically close
        return float(philza.read().split("\n")[0]) # The reason for the .split is in case creating the file has caused a new line to appear

def judgeWater(water):
    print(f"Vann: {water:.2f}L")
    if water < 500000:
        return "Det er lite vann igjen"
    elif water < 2000000:
        return "Det er en god mengde vann igjen"
    else:
        return "Blub blub blub (DET ER MER VANN IGJEN ENN VOLUMET PÅ SKIPET, HVORDAN???)"

vann = readWater("vann.txt")
print(judgeWater(vann))

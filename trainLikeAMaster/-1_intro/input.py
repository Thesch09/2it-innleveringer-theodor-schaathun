navn = input("Brave adventurer! What be yer name?\n")
if navn.lower == "jacob":
    print(f"Ah, so yer name be {navn}. What a stupid name")
else:
    print(f"Ah, so yer name be {navn}")

alder = input(f"And brave {navn}, how old are ye?\n")
ageOMatic = ""
try:
    alder = int(alder)
    if alder < 15:
        print("I take back what I said, yer too young!")
        ageOMatic = "older"
    elif alder > 150:
        print("Yer older than me granpappy, who's younger than me!")
        ageOMatic = "younger"
    else:
        print(f"So yer {alder} years old, ay. Great... just faboulus")
        ageOMatic = "older"
except ValueError:
    print("Ye can't even give me an actual number!?")

if ageOMatic == "":
    alder = 0
    print(f"Yer now {alder} years old, ye happy???")
if ageOMatic == "younger":
    alder -= alder*0.5
    print(f"Ye've un-aged to {alder}, ay. Likely storay")
if ageOMatic == "older":
    alder += alder*2
    print(f"Ye've aged to {alder}, ay. Likely storay")





































    # nothing to see up there
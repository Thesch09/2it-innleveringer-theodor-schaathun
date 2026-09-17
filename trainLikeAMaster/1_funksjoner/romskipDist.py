# Ingen AI/KI er brukt på denne oppgaven. Jeg, Theodor Schaathun, liker ikke å bruke det, jeg vil lære ting selv
# The sirens call of the balatro music from balatro being open and actually playing it's music (pretty good music) fills me with fuel to finish these far too simple tasks. I'm using more brainpower writing these funny little messages than actually doing the tasks

def calcTravel(speed, time):
    dist = speed * time
    print(f"Romskipet har reist {dist}km")
    if dist < 0:
        return "Du går bakveis\n"
    elif dist < 5000:
        return "Kort tur\n"
    elif dist < 20000:
        return "Middels tur\n"
    else:
        return "Lang tur\n"

print(calcTravel(-3,999))
print(calcTravel(10,90))
print(calcTravel(5000, 3))
print(calcTravel(10000, 10000))
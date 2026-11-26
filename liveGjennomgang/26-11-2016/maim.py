import hashlib
import secrets

brukernavn = "John Adminn"
passord = "Sup3rS3cr3t"

salt = secrets.token_bytes(16)
print(salt)

hashverdi = hashlib.sha256(salt + passord.encode()).hexdigest()

print(hashverdi)

inBN = input("Hva er brukernavn?\n").strip()
inP = hashlib.sha256(salt + input(f"Hva er passordet til {inBN}?\n").strip().encode()).hexdigest()

if brukernavn == inBN and hashverdi == inP:
    print("Velkommen! :D")
else:
    print("FEIL PASSORD OG/ELLER BRUKERNAVN")
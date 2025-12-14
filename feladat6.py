import random

print("Ez a program 20 véletlenszámot generál 1 és 12 között.")
print("Csak a 3-mal osztható számokat írja ki.")

darab = 0
szamlalo = 0

while szamlalo < 20:
    szam = random.randint(1, 12)
    if szam % 3 == 0:
        print(szam)
        darab += 1
    szamlalo += 1

print("Összesen", darab, "darab 3-mal osztható szám volt.")

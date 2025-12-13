print("Ez a program addig kér be páros számot, amíg a felhasználó páros számot nem ad meg.")

while True:
    szam = int(input("Kérlek, adj meg egy páros számot: "))
    if szam % 2 == 0:
        print(f"Köszönöm! A {szam} páros szám.")
        break
    else:
        print(f"A {szam} páratlan szám. Próbáld újra.")

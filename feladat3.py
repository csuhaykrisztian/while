print("Ez a program csökkenő sorrendben kiírja a páratlan számokat 1 és 10 között.")

for szam in range(10, 0, -1):
    if szam % 2 != 0:
        print(szam)

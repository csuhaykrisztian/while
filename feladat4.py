print("Ez a program a megadott szöveget a kívánt alkalommal írja ki.")

szoveg = input("Add meg a szöveget: ")
alkalom = int(input("Hányszor szeretnéd kiírni? "))

szamlalo = 1

while szamlalo <= alkalom:
    print(szamlalo, ". alkalom:", szoveg)
    szamlalo += 1


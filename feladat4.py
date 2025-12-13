print("Ez a program a bekért szöveget a felhasználó által megadott alkalommal írja ki.")

szoveg = input("Kérlek, írd be a szöveget: ")
alkalom = int(input("Hányszor szeretnéd kiírni a szöveget? "))

for i in range(alkalom):
    print(f"{i+1}. alkalom: {szoveg}")

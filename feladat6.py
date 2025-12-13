import random

print("Ez a program 20 véletlenszámot generál 1 és 12 között, majd kiírja csak a 3-mal osztható számokat.")

szamok = [random.randint(1, 12) for _ in range(20)]
harommal_oszthato = [sz for sz in szamok if sz % 3 == 0]

print("A 3-mal osztható számok:")
for sz in harommal_oszthato:
    print(sz)

print(f"Összesen {len(harommal_oszthato)} darab 3-mal osztható számot találtunk.")

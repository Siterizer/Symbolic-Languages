import random

tab = [[False for x in range(20)] for y in range(20)]
h = 20
for i in range(h):
    a = random.randint(0, 19)
    b = random.randint(0, 19)
    if tab[a][b] == False:
        tab[a][b] = True
    else:
        h += 1
zbior = set()
while True:
    x = int(input("Dawaj mnie x: "))
    y = int(input("Dawaj mnie y: "))
    if (x,y) in zbior:
        print("Juz tam szczelano")
    if (tab[x][y] == True):
        print("Trafiony")
        tab[x][y] = False
        zbior.add((x,y))
    else:
        print("Nie trafiony")
        zbior.add((x,y))


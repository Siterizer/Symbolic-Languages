def function1(slow):
    for i in slow:
        suma = 0
        for j in slow[i]:
            suma += slow[i][j]
        print(i, suma/len(slow[i]))
def function2(slow,kat):
    suma = 0
    h = 0
    for i in slow:
        for j in slow[i]:
            if(j == kat):
                suma += slow[i][j]
                h += 1
    print(kat," ",suma/h)








slownik = {"Adam": {"Matematyka": 5, "Biologia": 3, "Pszyrka": 4},
           "Tomek": {"Matematyka": 2, "Biologia": 2, "Pszyrka": 2},
           "Eryk": {"Matematyka": 5, "Biologia": 5, "Pszyrka": 5}}
function1(slownik)
function2(slownik,"Pszyrka")

import math


def function(slow):
    for i in slow:
        if slow[i] > 200:
            slow[i] = math.inf
        elif slow[i] > 0:
            slow[i] = 8 / (math.log10((slow[i])))
    return {x: slow[x] for x in slow if slow[x] > 0}


slownik = {"Adam": 20, "Mati": 50, "Arthas": 5646, "Pani Jadzia": -5}

print(function(slownik))

from random import randint


def function(tup1, tup2):
    for i in range(1, len(tup2)):
        tup1[i] *= tup2[i - 1]
    return tup1


typ1 = [randint(1, 20) for x in range(20)]
typ2 = [randint(1, 20) for x in range(18)]
print(function(typ1, typ2))

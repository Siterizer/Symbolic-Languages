import random as r


def function(list):
    list2 = [x for x in list]
    for i in range(1, len(list2) - 1):
        list2[i] = (list2[i - 1] + list2[i + 1]) / 2
    return list2


a = []
for i in range(20):
    a.append(r.randint(1, 20))

b = function(a)
print(b)

def function1(list):
    sum = 0
    for i in list:
        if i in "aeiouy":
            sum += 1
    return sum

def function2(words):
    return [x for x in words if function1(x) % 2 != 0]

print(function2(["one", "two", "milk", "yes","test","ee","e"]))

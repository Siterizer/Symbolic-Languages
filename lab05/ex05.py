from math import sqrt

print("Czesc powiedz mi modul pl czy en?")
ok = input()

if ok == "pl":
    import pl as help
else:
    import en as help
print(help.lang.get('hello'))
print(help.lang.get('info'))
k=int(input())
if k > 0:
    print(sqrt(k))
else:
    print(help.lang.get('error'))
print(help.lang.get('bye'))
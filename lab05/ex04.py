import random


with open("01_kto.txt") as f:
    pom = f.read()
    kto=pom.split("\n")
with open("02_co_zrobil.txt") as f:
    pom = f.read()
    co_zrobil=pom.split("\n")
with open("03_jaki.txt") as f:
    pom = f.read()
    jaki=pom.split("\n")
with open("04_co.txt") as f:
    pom = f.read()
    co=pom.split("\n")

def losuj():
    return "{} {} {} {} \n".format(random.choice(kto),random.choice(co_zrobil),random.choice(jaki),random.choice(co))

zapis = open("wyniki.txt","w")
for i in range(100):
    zapis.writelines(losuj())

import random

#Lista létrehoz

szamok = []

#Lista feltölt. 100 db random kétjegyű egész számmal
for i in range(100):
    szam = random.randint(10,99)
    szamok.append(szam)
    
#Ellenőrzés

print(szamok)
    

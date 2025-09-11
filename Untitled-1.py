
import random
#Lista feltölt. 100 db random kétjegyű egész számmal
szamok = []

for i in range(100):
    szam = random.randint(10,99)
    szamok.append(szam)
    
#Ellenőrzés

print(szamok)
    
#Egyszám játék
jatek_szam = 0
nem_talaldb = 0

kitalalando_szam = szamok[random.randint(0,len(szamok))]

#A Játék-------------------

jatszol= True



while(jatszol):
    
    tipp_sz = input("Tipped? (egész szám): ").strip()
    if(tipp_sz.isdecimal()):
        tipp = int(tipp_sz)
    else:
        print("Egész számmal!")
        continue
        
    while(tipp != kitalalando_szam):
        tipp_sz = input("Tipped? (egész szám): ").strip()
        if(tipp_sz.isdecimal()):
            tipp = int(tipp_sz)
        else:
            print("Egész szám!")
            continue
    
    print("Kitaláltad!")

    folytatas = input("Akarsz-e még játszani? [I/N]")
    if(folytatas == "N"):
        jatszol = False


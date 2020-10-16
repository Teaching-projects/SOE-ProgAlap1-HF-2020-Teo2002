"""
Irj programot, mely beker egy egesz szamot: n. Feltetelezhetjuk, hogy ez pozitiv. 

Ezt kovetoen kerjen be egesz szamokat addig, amig n db nemnegativ szamot nem kapott. 
A program a futasa vegen irja ki egy listaban ezeket a szamokat.

Pelda bemenet:
3
1
2
3
Pelda kimenet:
[1, 2, 3]

Pelda bemenet:
3
-1
0
-44
35
-19
-35
1
Pelda kimenet:
[0, 35, 1]

"""

n = int(input("Kérek egy számot: "))
lista = []
poz = 0
neg = 0
valtozo = 0
while valtozo != n:
    n2 = int(input("Kérek még egy számot: "))
    if n2 < 0:
        neg = n2
        valtozo -=1
    if n2 > 0:
        poz = n2
        lista.append(poz)
    valtozo+=1
print(lista)
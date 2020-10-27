"""
Keregessunk be pozitiv egesz szamokat addig, amig 0-t nem kapunk.
Ezutan irjuk ki, hogy melyik szam hanyszor szerepelt, egeszen a legnagyobb kapott szamig.

Pleda bemenet:
--------------------------------------------
1
1
2
1
5
0
--------------------------------------------


Pelda kimenet:
--------------------------------------------
1: 3
2: 1
3: 0
4: 0
5: 1
--------------------------------------------

Feltetelezhetjuk, hogy legalabb egy nem 0 szamot fogunk kapni.

"""
szam = 1
lista1 = []
lista2 = []

while szam!=0:
    szam = int(input())
    if szam not in lista1 and szam != 0:
        lista2.append(szam)
    if szam != 0:
        lista1.append(szam)

max = lista2[0]
for h in range(len(lista2)):
    if lista2[h] > max:
        max = lista2[h]

for i in range(1,max+1):
    print(str(i)+": "+str(lista1.count(i)))




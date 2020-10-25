"""
Kerj be egesz szamokat addig, amig 0-t nem kapsz.
A vegen irj ki minden bekert szamot, de mindgyiket csak egyszer, es abban a sorrendben, ahogy az elso elofordulas tortent.

pl:

Bemenet:
1
2
3
4
3
2
4
7
5
6
7
0
Kimenet:
1
2
3
4
7
5
6
"""

szam = []
no = ()
while no != 0:
    no = int(input("Adj meg egy szamot: "))
    if no not in szam:
        szam.append(no)
    elif no in szam:
        print("---> ", no, " Ez a szam mar a listaban van!")
    if no == 0:
        print("Listazas:")
        szam = szam[:-1] 
print("A szamjegyek sorrendben: ", szam)
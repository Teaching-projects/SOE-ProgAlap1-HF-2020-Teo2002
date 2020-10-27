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

number= []
no = ()

while no != 0:
    no = int(input())
    if no not in number:
        number.append(no)
    elif no in number:
        print("---> ", no)
    if no == 0:
        print()
        number = number[:-1] 

print(no)
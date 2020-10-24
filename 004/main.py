"""
Kerj be ket egesz szamot (feltetelezhetjuk, hogy pozitivak), es ird ki a legnagyobb kozos osztojukat, majd a legkisebb kozos tobbszorosuket.

pl:
Bemenet:
6
27
Kimenet:
3
54
"""

def legnko(n1, n2):
    while n2 != 0:
        (n1, n2) = (n2, n1 % n2)
    return n1

n1 = int(input("Az elso szam: "))
n2 = int(input("A masodik szam: "))
print("A ket szam legnagyobb kozos osztoja:",(legnko(n1, n2)))



    


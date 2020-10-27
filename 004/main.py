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

n1 = int(input())
n2 = int(input())
a = n1
b = n2

while n1 !=n2:
    if n1 > n2:
        n1 = n1 - n2
    else:
        n2 = n2 - n1

print(n1)
print(int(a*b/n1))






    


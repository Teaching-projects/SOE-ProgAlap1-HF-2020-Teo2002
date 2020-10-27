x=0.0
y=0.0

bemenet = No

while bemenet != "stop":
    if bemenet != "stop":
        szam = float(input())
    if bemenet == "forward":
        y += float(szam)
    elif bemenet == "backward":
        y -= float(szam)
    elif bemenet == "left":
        x -= float(szam)
    elif bemenet == "right":
        x += float(szam)

print(round(x,2))
print(round(y,2))
tavolsag = ((x**2)+(y**2))**(1/2)
print(round(tavolsag,2))

    
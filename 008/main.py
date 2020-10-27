x=0.0
y=0.0

def Tavolsag(x,y):
    print(round(((0 - x) ** 2 + (0 - y) ** 2) ** 0.5, 2))
    
while True:
    irany = str(input())
    if irany == "stop": 
        break
    egyseg = float(input())
    if irany == "forward": 
        y = y + egyseg
    if irany == "backward": 
        y = y - egyseg
    if irany == "right": 
        x = x + egyseg
    if irany == "left": 
        x = y - egyseg
        
print(round(x,2))
print(round(y,2))
Tavolsag(x,y)
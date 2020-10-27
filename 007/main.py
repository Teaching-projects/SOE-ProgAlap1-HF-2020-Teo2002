egyenleg = 0
szamldij = 2000
negativ = 1.1 
pozitiv = 1.05 
osszeg = 0
penzmozgas = int(input()) 
egyenleg += penzmozgas 
osszeg += penzmozgas
if egyenleg > 0:
  egyenleg *= pozitiv
else:
  egyenleg *= negativ
egyenleg = int(egyenleg)
i = 0
while i < 11:
    penzmozgas = int(input())
    osszeg += penzmozgas
    egyenleg -= szamldij
    egyenleg +=penzmozgas
    if egyenleg > 0:
        egyenleg *= pozitiv  
    else:
        egyenleg *= negativ
    egyenleg = int(egyenleg)
    i += 1
print(egyenleg)
print(osszeg)

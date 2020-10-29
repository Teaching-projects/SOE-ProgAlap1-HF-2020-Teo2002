honap = 0
total = 0
perc = []
sms = []
szamla = []

while honap != 12:
    perc.append(int(input()))
    sms.append(int(input()))
    honap += 1
csomhav = int(input())
csomperc = int(input())
csomsms = int(input())

for i in range(len(perc)):
    if perc[i]*csomperc + sms[i]*csomsms < csomhav: szamla.append(csomhav)
    else: szamla.append(perc[i]*csomperc + sms[i]*csomsms)
for i in range(len(szamla)):
    total += szamla[i]

print(szamla)
print(total)


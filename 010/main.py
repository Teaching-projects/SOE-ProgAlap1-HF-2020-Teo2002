total = 0
honap = 12
perc = []
sms = []
szamla = []

for i in range(honap):
    telperc = int(input())
    sms = int(input())
    percek.append(telperc)
    smsek.append(sms)


csomhav = int(input())
csomperc = int(input())
csomsms = int(input())

for i in range(honap):
    most = 0
    if (csomperc * percek[i]) + (csomsms * smsek[i]) > csomhav:
        most += (csomperc * percek[i]) + (csomsms * smsek[i])
    else: most += csomhav
    szamla.append(most)
    total += most

print(szamla)
print(total)


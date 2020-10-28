jantel = int(input())
jansms = int(input())
febrtel = int(input())
febrsms = int(input())
marctel = int(input())
marcsms = int(input())
aprtel = int(input())
aprsms = int(input())
majtel = int(input())
majsms = int(input())
juntel = int(input())
junsms = int(input())
jultel = int(input())
julsms = int(input())
augtel = int(input())
augsms = int(input())
septtel = int(input())
septsms = int(input())
okttel = int(input())
oktsms = int(input())
novtel = int(input())
novsms = int(input())
dectel = int(input())
decsms = int(input())

csomhav = int(input())
csomperc = int(input())
csomsms = int(input())

janosszeg = (jantel * csomperc) + (jansms * csomsms)
if janosszeg <1000:
    print (1000)
else:
    print (janosszeg)

febrosszeg = (febrtel * csomperc) + (febrsms * csomsms)
if febrosszeg <1000:
    print (1000)
else:
    print (febrosszeg)

marcosszeg = (martel * csomperc) + (marcsms * csomsms)
if marcosszeg <1000:
    print (1000)
else:
    print (marcosszeg)

aprosszeg = (aprtel * csomperc) + (aprsms * csomsms)
if janosszeg <1000:
    print (1000)
else:
    print (aprosszeg)

majosszeg = (majtel * csomperc) + (majsms * csomsms)
if janosszeg <1000:
    print (1000)
else:
    print (majosszeg)

junosszeg = (juntel * csomperc) + (junsms * csomsms)
if junosszeg <1000:
    print (1000)
else:
    print (junosszeg)

julosszeg = (jultel * csomperc) + (julsms * csomsms)
if julosszeg <1000:
    print (1000)
else:
    print (julosszeg)

augosszeg = (augtel * csomperc) + (augsms * csomsms)
if augosszeg <1000:
    print (1000)
else:
    print (augosszeg)

septosszeg = (septtel * csomperc) + (septsms * csomsms)
if septosszeg <1000:
    print (1000)
else:
    print (septosszeg)

oktosszeg = (okttel * csomperc) + (oktsms * csomsms)
if oktosszeg <1000:
    print (1000)
else:
    print (oktosszeg)

novosszeg = (novtel * csomperc) + (novsms * csomsms)
if novosszeg <1000:
    print (1000)
else:
    print (novosszeg)

decosszeg = (dectel * csomperc) + (decsms * csomsms)
if decosszeg <1000:
    print (1000)
else:
    print (decosszeg)

szamla=[]
szamla.append(janosszeg)
szamla.append(febrosszeg)
szamla.append(marcosszeg)
szamla.append(aprosszeg)
szamla.append(majosszeg)
szamla.append(junosszeg)
szamla.append(julosszeg)
szamla.append(augosszeg)
szamla.append(septosszeg)
szamla.append(oktosszeg)
szamla.append(novosszeg)
szamla.append(decosszeg)

valtozo = 0
while valtozo < len(szamla):
    aktualis = szamla[valtozo]
    sum += aktualis
    valtozo += 1
print(sum)



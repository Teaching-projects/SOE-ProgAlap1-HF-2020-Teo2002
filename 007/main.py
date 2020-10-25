honap = [] 
bank = []
savev = []
szvd= float() 
kd = float() 
startb = float() 
starth = float() 
pm = float() 
pk = float() 
nk = float()
eh = float() 
eb = float()

def szamolj(pm) :
    startb = bank[-1]
    starth = honap[-1]
    kd = savev[0]
    if kd <= 0 : startb = startb + pm + szvd
    if kd > 0 : startb = startb + pm; kd = kd - 1
    if startb > 0 : startb = startb * pk
    if startb < 0 : startb = startb - ((startb * -1) * nk)
    if startb == 0 : startb = startb
    savev[0] = kd
    bank.append(int(startb))
    honap.append((int(starth)) + pm)
    if savev[1] == "i": print("Havi banki egyenleg:",bank[-1] ,"Ft.   ","bank nelkul:", honap[-1], "Ft.")
print("Bankszamla adatok")
print("---------------------------------------------------------------------")
bank.append(float(input("Indulo egyenleg: ")))
honap.append(bank[0])
szvd = float(input("Szamla vezetesi dij: "))
savev.append(int(input("kedvezmenyes honapok szama: ")))
szvd = szvd * -1
savev.append(str(input("Honapos lebontas? i/n: ")))
print("---------------------------------------------------------------------")
pm = float(input("Januar penz mozgas: "))
szamolj(pm)
pm = float(input("Februar penz mozgas: "))
szamolj(pm)
pm = float(input("Marcius penz mozgas: "))
szamolj(pm)
pm = float(input("Aprilis penz mozgas: "))
szamolj(pm)
pm = float(input("Majus penz mozgas: "))
szamolj(pm)
pm = float(input("Junius penz mozgas: "))
szamolj(pm)
pm = float(input("Julius penz mozgas: "))
szamolj(pm)
pm = float(input("Augusztus penz mozgas: "))
szamolj(pm)
pm = float(input("Szeptember penz mozgas: "))
szamolj(pm)
pm = float(input("Oktober penz mozgas: "))
szamolj(pm)
pm = float(input("November penz mozgas: "))
szamolj(pm)
pm = float(input("December penz mozgas: "))
szamolj(pm)
print("---------------------------------------------------------------------")
print("Eves zaras a banknal: ",bank[-1] , "Ft.")
print("Eves zaras a bank nelkul: ",honap[-1] , "Ft.")

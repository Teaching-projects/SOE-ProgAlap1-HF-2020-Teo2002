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
    if savev[1] == "i": print(bank[-1] ,"Ft.", honap[-1], "Ft.")
print()
print("---------------------------------------------------------------------")
bank.append(float(input()))
honap.append(bank[0])
szvd = float(input())
savev.append(int(input()))
szvd = szvd * -1
savev.append((input()))
print("---------------------------------------------------------------------")
pm = float(input())
szamolj(pm)
pm = float(input())
szamolj(pm)
pm = float(input())
szamolj(pm)
pm = float(input())
szamolj(pm)
pm = float(input())
szamolj(pm)
pm = float(input())
szamolj(pm)
pm = float(input())
szamolj(pm)
pm = float(input())
szamolj(pm)
pm = float(input())
szamolj(pm)
pm = float(input())
szamolj(pm)
pm = float(input())
szamolj(pm)
pm = float(input())
szamolj(pm)
print("---------------------------------------------------------------------")
print(bank[-1] , "Ft.")
print(honap[-1] , "Ft.")

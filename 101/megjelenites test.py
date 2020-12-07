def megjelenites(szo, betuk):
    """Visszaad egy olyan szót, amiben a betuk`-ben lévő betűk látszanak, minden más helyére 
 kerül, kivéve néhány speciális karaktert, amik megjelennek változtatás nélkül. Ezen karakterek listája a specialis_karakterek` globális listában adott.
    Kis és nagy betűket megkülönbözteti a függvény.
    Args:
        szo (str): a szó, aminek megjelenített változatát meg szeretnénk kapni. 
        betuk (Tippek): Egy karakterből, betűkből álló lista, amit már tippeltünk
    Returns:
        str: a megjelenített változata a szónak
    """
    megjelenszo=[]
    for i in range(len(betuk)):
        if betuk[i] in szo:
            megjelenszo.append(betuk[i])
        else: 
            megjelenszo.append('_')
    return megjelenszo

betuk = ["a","b","c","d"]
szo=input()
print(megjelenites(szo, betuk))
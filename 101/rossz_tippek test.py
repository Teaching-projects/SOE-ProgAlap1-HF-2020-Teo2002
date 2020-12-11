def rossz_tippek(szo:str, betuk:list):
    """Megadja, hogy hány rossz betűt tippeltünk eddig.

    Args:
        szo (str): a kitalálandó szó
        betuk (Tippek): az eddigi betű tippjeink

    Returns:
        int: a rossz tippek száma
    """
    elhasznalt = (0)
    for i in range(len(betuk)): 
        if betuk[i] not in szo:
            elhasznalt = elhasznalt+1 
    return elhasznalt

szo=()
betuk = ["a","b","d","c"]
print(rossz_tippek(szo, betuk))
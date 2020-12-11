def tartalmazza(szo:str, betu:str) -> bool:
    """Megadja, hogy a megaadott betű szerepel-e a megadott szóban.

    Args:
        szo (str): a szó
        betu (str): a betű, amit keresünk, feltételezhető, hogy 1 karakter hosszú

    Returns:
        bool: `True` ha szerepel, `False` ha nem    
    """
    if betu in szo:
        return True
    else:
        return False
    
szo = ()
betu=input()
betuk = ["a","b","d","c"]
print(betuk,betu)
print(tartalmazza(szo, betu))
def kozte_van(betu, betuk):
    """Megadja, hogy a listában már benne van-e a megadott betű, vagy sem.
    Args:
        betu (str): a keresett betű
        betuk (Tippek): betűk listája
    Returns:
        bool: True ha benne van, False ha nincsen.
    """
    for i in range (len (betuk)):
        if betu == betuk[i]:
            return True
        else:
            return False

betu=input()
betuk = ["a","b","d","c"]
print(betuk,betu)
print(kozte_van(betu, betuk))

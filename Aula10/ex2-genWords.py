
# Generates all length-3 words with symbols taken from the given alphabet.
def genWords3(symbols):
    return [ x+y+z for x in symbols for y in symbols for z in symbols ]


# Generates all length-n words with symbols taken from the given alphabet.
"""def genWords(symbols, n):
    lst=list(symbols)
    if n > 1:
        lst= [simbolo+palavra for simbolo in symbols for palavra in genWords(symbols, n-1)]
    return lst"""

def genWords(symbols, n):
    if n == 1:
        return list(symbols)
    return [simbolo+palavra for simbolo in symbols for palavra in genWords(symbols, n-1)]


def main():
    lstA = genWords3("abc")
    print(lstA)

    lstB = genWords("abc", 3)  # should return the same words, maybe in other order
    print(lstB)
    assert sorted(lstA) == sorted(lstB)

    lstC = genWords("01", 4)  # should return all length-4 binary words
    print(lstC)
    
if __name__ == "__main__":
    main()


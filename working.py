
allmen = {
    "a": ["o", "m", "n", "l", "p"],
    "b": ["p", "n", "m", "l", "o"],
    "c": ["m", "p", "l", "o", "n"],
    "d": ["p", "m", "o", "n", "l"],
    "e": ["o", "l", "m", "n", "p"]
}
allwomen = {
    "l": ["d", "e", "b", "c", "a"],
    "m": ["b", "a", "d", "c", "e"],
    "n": ["a", "c", "e", "d", "b"],
    "o": ["d", "a", "c", "b", "e"],
    "p": ["b", "e", "a", "c", "d"]}

wifeof = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0
}

husbandof = {
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0
}


def engage(guy, girl):
    husbandof[girl] = guy
    wifeof[guy] = girl
    print(f"{guy} and {girl} engaged")


def breakup(guy, girl):
    wifeof[guy] = 0
    husbandof[girl] = 0
    print(f"{guy} and {girl} broke up")


while not all(value != 0 for value in wifeof.values()):
    for man in allmen.keys():
        if wifeof[man] == 0:
            for pref in allmen[man]:
                if husbandof[pref] == 0:
                    engage(man, pref)
                    break
                elif husbandof[pref] != 0 and allwomen[pref].index(man) < allwomen[pref].index(husbandof[pref]):
                    print(f"As {pref} favours {man} over {husbandof[pref]}")
                    breakup(husbandof[pref], pref)
                    engage(man, pref)
                    break

print(wifeof)

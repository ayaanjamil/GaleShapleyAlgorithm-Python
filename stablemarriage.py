import json

data = json.load(open("d.json"))

allmen = data["men"]
allwomen = data["women"]

wifeof = {
}

husbandof = {
}


def engage(guy, girl):
    husbandof[girl] = guy
    wifeof[guy] = girl
    print(f"{guy} and {girl} engaged")


def breakup(guy, girl):
    wifeof[guy] = 0
    husbandof[girl] = 0
    print(f"{guy} and {girl} broke up")


def initialize():
    for i in allmen.keys():
        wifeof[i] = 0
    for i in allwomen.keys():
        husbandof[i] = 0


def main():
    while not all(value != 0 for value in wifeof.values()):
        for man in allmen.keys():
            if wifeof[man] == 0:
                for pref in allmen[man]:
                    if husbandof[pref] == 0:
                        engage(man, pref)
                        break
                    elif husbandof[pref] != 0 and allwomen[pref].index(man) < allwomen[pref].index(husbandof[pref]):
                        print(
                            f"As {pref} favours {man} over {husbandof[pref]}")
                        breakup(husbandof[pref], pref)
                        engage(man, pref)
                        break


initialize()
main()
print(wifeof)

data = json.load(open("matches.json"))
data["data"] = wifeof
with open("matches.json", "w") as f:
    json.dump(data, f, indent=4)

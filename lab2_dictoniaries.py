dict = {"imie" : "kowalski", "nazwisko" : "kowalski", "wiek": "15"}

#print(dict)


def flip_dict(d):
    ndict = {}
    for key, value in d.items():
        ndict.setdefault(value, []).append(key)
    return ndict


print(flip_dict(dict))
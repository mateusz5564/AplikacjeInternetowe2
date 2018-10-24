def is_cyclone_phrase(phrase):
    jest = True
    c = 1
    x = 0
    mid = int(phrase.__len__() / 2)
    if phrase.__len__() == 0:
        jest = True
    else:
        if phrase[x] > phrase[phrase.__len__() - c]:
            jest = False

        for x in range(1, mid + 1):
            if phrase.__len__() - c == x:
                break
            if phrase[phrase.__len__() - c] > phrase[x]:
                jest = False
            c += 1
            if phrase.__len__() - c <= x:
                break
            else:
                if phrase[x] > phrase[phrase.__len__() - c]:
                    jest = False

    print(jest)


is_cyclone_phrase("adjourned")
is_cyclone_phrase("settled")
is_cyclone_phrase("all alone at noon")
is_cyclone_phrase("by myself at twelve pm")
is_cyclone_phrase("acb")
is_cyclone_phrase("")

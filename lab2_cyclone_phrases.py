def cyclone_word(word):
    word = word.upper()
    letters = [None] * len(word)
    half = (len(word) + 1) // 2
    letters[::2] = word[:half]
    letters[1::2] = word[:half - 1:-1]
    return all([left <= right for left, right in zip(letters, letters[1:])])


def cyclone_phrase(phrase):
    return all([cyclone_word(word) for word in phrase.split()])

print(cyclone_phrase("adjourned"))
print(cyclone_phrase("settled"))
print(cyclone_phrase("all alone at noon"))
print(cyclone_phrase("by myself at twelve pm"))
print(cyclone_phrase("acb"))
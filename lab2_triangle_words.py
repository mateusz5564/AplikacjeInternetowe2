

def is_triangle_word(word):
    sum = 0
    for ch in word.upper().strip():
        sum += ord(ch) - ord('A')+1
    for x in triangle_numbers():
        if sum == x:
            return True

def triangle_numbers():
    lista = []
    for i in range(100):
        x = i*(i+1)/2
        lista.append(x)
    return lista


def nr_tr_words():
    file = open("words.txt", "r")
    lines = file.readlines()

    slowa = [line.upper().strip() for line in lines if is_triangle_word(line)]
    print(slowa)
    print(len(slowa))

nr_tr_words()



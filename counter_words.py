from collections import defaultdict


def counter_words(file, top_n):
    counter = defaultdict(lambda: 0)
    with open(file, encoding='UTF-8') as text:
        for line in text:
            if line:
                token = line.split()
                for words in token:
                    if words not in '()!?.,;:"-_@#$/':  # wykluczam kiedy znaki interpunkcyjne są traktowane jako słowa
                        word = ''
                        for char in words:
                            if char not in '()!?.,;:"-_@#$/':  # wydobycie samych słów bez znaków interpunkcyjnych
                                word += char
                        word = word.lower()  # wielkość liter nie ma znaczenia
                        counter[word] += 1

    top = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    while True:
        if top[top_n][1] == top[top_n+1][1]:
            top_n += 1
        else:
            break
    print(top_n, 'najczęściej występujących słów to: ', top[:top_n])

    # -------------DLA SPRAWDZENIA--------------
    # najrzadziej występujące słowa bo np. 1 występuje dużo razy więc sprawdzę czy działa ta część zadania
    # 'jeśli słowa na pozycji n+1 i n+2 wystąpiły tyle samo razy co to na pozycji n, to także mają zostać wyświetlone'

    rare = sorted(counter.items(), key=lambda x: x[1])
    while True:
        if rare[top_n][1] == rare[top_n+1][1]:
            top_n += 1
        else:
            break
    print(top_n, 'najrzadziej występujących słów to: ', rare[:top_n])


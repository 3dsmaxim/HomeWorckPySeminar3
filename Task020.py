AlphabitEn = \
    {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1,
     'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4,
              'y': 4, 'k': 5, 'j': 8, 'x': 8, 'q': 10, 'z': 10, }
AlphabitRu = \
    {'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1, 'о': 1, 'р': 1, 'с': 1, 'т': 1, 'д': 2,
     'к': 2, 'л': 2, 'м': 2, 'п': 2, 'у': 2, 'б': 3, 'г': 3, 'ё': 3, 'ь': 3, 'я': 3,
     'й': 4, 'ы': 4, 'ж': 5, 'з': 5, 'х': 5, 'ц': 5, 'ч': 5, 'ш': 8, 'э': 8, 'ю': 8,
     'ф': 10, 'щ': 10, 'ъ': 10, }


def NumEnter(n, e, r):
    en = 0
    ru = 0
    while True:

        if n.isalpha():
            for i in range(0, len(n)):
                if n[i] in e.keys():
                    en += 1
                if n[i] in r.keys():
                    ru += 1
            if en == 0:
                break
            if ru == 0:
                break
            if en > 0 and ru > 0:
                n = input('Все буквы в слове нужно ввести на одном языке \
                \nвведите слово: ').lower()
                en = 0
                ru = 0
        else:
            n = input('Ведите слово без цифр: ')
    return n


word = NumEnter(input('Введите слово: ').lower(),AlphabitEn, AlphabitRu)

sum = 0
for i in range(0, len(word)):
    if word[i] in AlphabitEn.keys():
        sum += AlphabitEn[word[i]]
    if word[i] in AlphabitRu.keys():
        sum += AlphabitRu[word[i]]


print(f'{sum} очков')

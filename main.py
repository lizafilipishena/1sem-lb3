while True:
    vowelRus = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    vowelRUS = ['А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
    vowelEng = ['a', 'e', 'i', 'o', 'u', 'y']
    vowelENG = ['A', 'E', 'I', 'O', 'U', 'Y']

    text = str(input('Введите текст: '))

    for i in range(len(vowelRus)):
        cnt = 0
        for j in text:
            if j == vowelRus[i] or j == vowelRUS[i]:
                cnt += 1

        if cnt != 0:
            print('Кол-во', vowelRus[i], '-', cnt)

    for i in range(len(vowelEng)):
        cnt = 0
        for j in text:
            if j == vowelEng[i] or j == vowelENG[i]:
                cnt += 1

        if cnt != 0:
            print('Quantity', vowelEng[i], '-', cnt)

    max_cnt = 0
    result = []
    for i in range(len(text.split())):
        word = text.split()[i]
        cnt = 0
        for j in word:
            if (j in ''.join(vowelRus)) or (j in ''.join(vowelRUS)) or (j in ''.join(vowelEng)) or (j in ''.join(vowelENG)):
                cnt += 1
        if cnt == max_cnt:
            result.append(word)
        if cnt > max_cnt:
            result.clear()
            max_cnt = cnt
            result.append(word)

    print('Слова(о) с максимальным количеством гласных букв:', ' '.join(result))
    print('Кол-во гласных букв: ', max_cnt)
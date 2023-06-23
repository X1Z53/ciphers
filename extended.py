# Шифр Цезаря
def caesar_cipher(text, key):
    """
        Описание шифра Цезаря

        Получаемые данные:
        text - не зашифрованный текст; string
        key - ключ, сдвиг; integer

        Возвращаемые данные:
        result - зашифрованный текст; string
    """

    lower = "abcdefghijklmnopqrstuvwxyz"  # Алфавит из символов нижнего регистра
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Алфавит из символов верхнего регистра
    alphabet = lower + upper              # Алфавит из символов обоих регистров (сначала нижний)

    shifted_lower = lower[key:] + lower[:key]         # Алфавит со сдвигом из символов нижнего регистра
    shifted_upper = upper[key:] + upper[:key]         # Алфавит со сдвигом из символов верхнего регистра
    shifted_alphabet = shifted_lower + shifted_upper  # Алфавит со сдвигом из символов обоих регистров (сначала нижний)

    shifting = {}                                 # Создание сдвига для шифровки
    for i, j in zip(alphabet, shifted_alphabet):  # Начало цикла, в котором i и j будут одновременно идти по alpabet и
        shifting[i] = j                           # shifted_alphabet соответственно

    result = ""  # Создание переменной для итогового текста

    for i in text:                 # Начало цикла, в котором i будет принимать значение каждого символа text поочерёдно
        if i.isalpha():            # Если символ является буквой
            result += shifting[i]  # Прибавляем к итоговому тексту сдвинутый символ, соответствущий символу i
        else:                      # Иначе
            result += i            # Прибавляем к итоговому тексту символ i

    return result  # Возвращение итогового текста


# Шифр Атбаш
def atbash_cipher(text):
    """
        Описание шифра Атбаш

        Получаемые данные:
        text - не зашифрованный текст; string

        Возвращаемые данные:
        result - зашифрованный текст; string
    """

    lower = "abcdefghijklmnopqrstuvwxyz"           # Алфавит из символов нижнего регистра
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"           # Алфавит из символов верхнего регистра
    alphabet = lower + upper                       # Алфавит из символов обоих регистров (сначала нижний)
    reversed_alphabet = lower[::-1] + upper[::-1]  # Перевёрнутый алфавит из символов обоих регистров (сначала нижний)

    shifting = {}                                  # Подготовка места для сдвига шифровки
    for i, j in zip(alphabet, reversed_alphabet):  # Начало цикла, в котором i и j будут одновременно идти
        shifting[i] = j                            # по alphabet и reversed_alphabet соответственно

    result = ""  # Создание места для итогового текста

    for i in text:                 # Начало цикла, в котором i будет принимать значение каждого символа text поочерёдно
        if i.isalpha():            # Если символ является буквой
            result += shifting[i]  # Прибавляем к итоговому тексту сдвинутый символ, соответствущий символу i
        else:                      # Иначе
            result += i            # Прибавляем к итоговому тексту символ i

    return result  # Возвращение итогового текста


# Шифр ограждения рельса
def rail_fence_cipher(text, key):
    """
        Описание шифра ограждения рельса

        Получаемые данные:
        text - не зашифрованный текст; string
        key - ключ, количество рельс; integer

        Возвращаемые данные:
        result - зашифрованный текст; string
    """

    rails = []                      # Подготовка для создания матрицы
    for i in range(key):            # Запуск цикла
        rails.append([])            # Создаём пустой вложенный массив

    move_down = False  # Подготовка значения для определения направления движения
    row = 0    # Определяем координаты первой ячейки в матрице

    for i in range(len(text)):         # Начинаем цикл
        if row == 0 or row == key-1:   # Если сейчас идёт работа с первым или последним рельсом
            move_down = not move_down  # Изменить направление движения

        rails[row].append(text[i])  # Записываем в ряд символ строки

        if move_down:  # Если идёт движение вниз
            row += 1   # опускаемся на одну строку
        else:          # Иначе
            row -= 1   # поднимаемся на одну строку

    result = ""                         # Подготовка места для результата
    for i in range(key):                # Двумя циклами проходимся по
        for j in range(len(rails[i])):  # всей двумерной матрице
            result += rails[i][j]       # добавить эту ячейку в результат

    return result  # Вернуть результат


# Шифр Скитала
def scytale_cipher(text, key):
    """
        Описание шифра Скиталы

        Получаемые данные:
        text - не зашифрованный текст; string
        key - ключ, количество строчек; integer

        Возвращаемые данные:
        result - зашифрованный текст; string
    """

    rows = []                      # Подготовка для создания матрицы
    for i in range(key):            # Запуск цикла
        rows.append([])            # Создаём пустой вложенный массив

    row = 0    # Определяем координаты первой ячейки в матрице

    for i in range(len(text)):         # Начинаем цикл
        rows[row].append(text[i])  # Записываем в ряд символ строки

        row += 1   # опускаемся на одну строку

        if row == key:
            row = 0

    result = ""                         # Подготовка места для результата
    for i in range(key):                # Двумя циклами проходимся по
        for j in range(len(rows[i])):  # всей двумерной матрице
            result += rows[i][j]       # добавить эту ячейку в результат

    return result  # Вернуть результат


# Шифр Виженера
def vigenere_cipher(text, key):
    """
        Описание шифра Виженера

        Получаемые данные:
        text - не зашифрованный текст; string
        key - ключ, кодовое слово; string

        Возвращаемые данные:
        result - зашифрованный текст; string
    """

    lower = "abcdefghijklmnopqrstuvwxyz"  # Алфавит из символов нижнего регистра
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Алфавит из символов верхнего регистра
    alphabet = lower + upper              # Алфавит из символов обоих регистров (сначала нижний)

    vigenere_table = []                                                   # Подготовка места для таблицы Виженера
    for i in range(len(lower)):                                           # Цикл для создания таблицы Виженера
        shifted_alphabet = lower[i:] + lower[:i] + upper[i:] + upper[:i]  # Создание смещённого алфавита
        vigenere_table.append(shifted_alphabet)                           # Добавление смещённого алфавита в таблицу

    i = 0                         # Создание итерационной переменной
    while len(key) != len(text):  # Если длина ключа не равна длине текста без учёта пробелов
        key += key[i]             # к ключу прибавить символ ключа
        i += 1                    # и увеличить итерационную переменную

    result = ""                                                         # Подготовка места для результата
    non_alpha_count = 0                                                 # Количество символов, не входящих в алфавит
    for idx, item in enumerate(text):                                   # Цикл по исходному тексту
        if item in alphabet:                                            # Если символ - это буква
            key_index = alphabet.index(key[idx-non_alpha_count]) % 26   # Индекс символа ключа в алфавите
            text_index = alphabet.index(item)                           # Индекс символа в алфавите
            result += vigenere_table[key_index][text_index]             # К результату прибавить символ на пересечении
        else:                                                           # Иначе
            non_alpha_count += 1                                        # Увеличение количества неалфавитных символов
            result += item                                              # К результату прибавить символ

    return result  # Вернуть итог

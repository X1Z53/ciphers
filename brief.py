from string import ascii_lowercase as lower, ascii_uppercase as upper, ascii_letters as alphabet


# Шифр Цезаря
def caesar_cipher(text, key):
    return text.translate(str.maketrans(alphabet, lower[key:] + lower[:key] + upper[key:] + upper[:key]))


# Шифр Атбаш
def atbash_cipher(text):
    return text.translate(str.maketrans(alphabet, lower[::-1] + upper[::-1]))


# Зигзагообразный шифр
def rail_fence_cipher(text, key):
    matrix, move_down, row = [[] for _ in range(key)], False, 0

    for i in range(len(text)):
        if row in [0, key - 1]:
            move_down = not move_down
        matrix[row].append(text[i])
        row += [-1, 1][move_down]

    return "".join([matrix[i][j] for i in range(key) for j in range(len(matrix[i])) if matrix[i][j]])


# Шифр Скитала
def scytale_cipher(text, key):
    matrix, row = [[] for _ in range(key)], 0

    for i in range(len(text)):
        matrix[row].append(text[i])
        row = 0 if row == key-1 else row+1

    return "".join([matrix[i][j] for i in range(key) for j in range(len(matrix[i])) if matrix[i][j]])


# Шифр Виженера
def vigenere_cipher(text, key):
    vigenere_table = [lower[i:] + lower[:i] + upper[i:] + upper[:i] for i in range(len(lower))]
    key = "".join(key[i % len(key)]for i in range(len(text.replace(" ", ""))))

    result, non_alpha_count = "", 0
    for idx, item in enumerate(text):
        if item in alphabet:
            key_index, text_index = alphabet.index(key[idx - non_alpha_count]) % 26, alphabet.index(item)
            result += vigenere_table[key_index][text_index]
        else: non_alpha_count, result = non_alpha_count + 1, result + item

    return result
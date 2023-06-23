from colorama import Fore, Back, init
from functions import go_test
from os import system
from random import randint, choice
from string import ascii_letters, digits
from brief import caesar_cipher, atbash_cipher
from with_libraries import rail_fence_cipher, scytale_cipher, vigenere_cipher
init()
system("cls")
system("title Шифратор")

ciphers_func_names = {"Шифр Атбаш (Atbash cipher)": "Atbash",
                      "Шифр Виженера (Vigenere cipher)": "Vigenere",
                      "Шифр Скиталы (Scytale cipher)": "Scytale",
                      "Шифр ограничения рельса (Rail Fence cipher)": "Rail Fence",
                      "Шифр Цезаря (Caesar cipher)": "Caesar"}

ciphers = {0: "Шифр Атбаш (Atbash cipher)",
           1: "Шифр Виженера (Vigenere cipher)",
           2: "Шифр Скиталы (Scytale cipher)",
           3: "Шифр ограничения рельса (Rail Fence cipher)",
           4: "Шифр Цезаря (Caesar cipher)"}

actions = {0: "Тестирование скорости шифров",
           1: "Все шифры в по очереди порядке",
           2: "Все шифры в случайном порядке",
           3: "Выбрать шифр"}

[print(Back.BLACK + Fore.LIGHTYELLOW_EX + str(key) + ": " + Fore.YELLOW + actions[key]) for key in actions]
action = input(Fore.RED + "\nВыберите действие (пусто - \"выбрать шифр\"): " + Fore.LIGHTRED_EX)
action = 3 if action == "" else int(action)
print("\n" + Fore.CYAN + actions[action] + "\n")

if not action:
    ciphers[5] = "Тестировать всё"
    [print(Fore.LIGHTMAGENTA_EX + str(i) + ": " + Fore.MAGENTA + ciphers[i]) for i in ciphers]
    test = input(Fore.RED + "\nЧто тестировать? (пусто - тестировать всё): " + Fore.LIGHTRED_EX)
    test = 5 if test == "" else int(test)
    repeats = 1
    if test != 5: repeats = input(Fore.RED + "Сколько раз? (пусто - 1 раз): " + Fore.LIGHTRED_EX)
    repeats = 1 if repeats == "" else int(repeats)
    print(Fore.CYAN + "\nПридётся немного подождать...")

    if test == 5:
        print(Fore.GREEN + "\n\nШифр Атбаш", end="")
        go_test("Atbash")
        print(Fore.LIGHTBLUE_EX + "\n\nШифр Виженера", end="")
        go_test("Vigenere")
        print(Fore.YELLOW + "\n\nШифр Скиталы", end="")
        go_test("Scytale")
        print(Fore.LIGHTYELLOW_EX + "\n\nШифр ограничения рельса", end="")
        go_test("Rail Fence")
        print(Fore.LIGHTGREEN_EX + "\n\nШифр Цезаря", end="")
        go_test("Caesar")
    else:
        print(ciphers[test], end="")
        go_test(ciphers_func_names[ciphers[test]], repeats)

elif action == 1:
    [print(Fore.LIGHTMAGENTA_EX + str(i) + ": " + Fore.MAGENTA + ciphers[i]) for i in range(5)]
    order = input(Fore.RED + "\nВведите порядок шифров (пусто - случайный набор шифров): " + Fore.LIGHTRED_EX) or\
            [choice(range(5)) for _ in range(5)]
    if type(order) == str: order = list(map(int, order))
    text = input(Fore.RED + "Исходный текст (пусто - случайный набор символов): " + Fore.LIGHTRED_EX) or \
           ''.join(choice(ascii_letters + digits) for _ in range(100))
    for i in order:
        func = eval(ciphers_func_names[ciphers[i]].lower().replace(" ", "_") + "_cipher")
        if i: key = randint(2, len(text)) if i != 1 else "".join(choice(ascii_letters)
                                                                 for i in range(min(len(text), 25)))

        text = f"{key}{func(text, key)}" if i else func(text)
    print(text)

elif action == 2:
    count = input(Fore.RED + "Введите количество шифров (пусто - случайное число): " + Fore.LIGHTRED_EX)
    count = randint(1, 10) if count == "" else int(count)
    order = [randint(0, len(ciphers_func_names)-1) for i in range(count)]
    text = input(Fore.RED + "Исходный текст (пусто - случайный набор символов): " + Fore.LIGHTRED_EX) or \
           ''.join(choice(ascii_letters + digits) for _ in range(100))
    for i in order:
        func = eval(ciphers_func_names[ciphers[i]].lower().replace(" ", "_") + "_cipher")
        if i: key = randint(2, len(text)) if i != 1 else "".join(choice(ascii_letters)
                                                                 for i in range(min(len(text), 25)))

        text = f"{key}{func(text, key)}" if i else func(text)

    print(text)

elif action == 3:
    [print(Fore.LIGHTYELLOW_EX + str(key) + ": " + Fore.YELLOW + ciphers[key]) for key in ciphers]
    cipher = input(Fore.RED + "\nВыберите шифр (пусто - случайный шифр): " + Fore.LIGHTRED_EX)
    cipher = ciphers[randint(0, len(ciphers))] if cipher == "" else int(cipher)
    print(Fore.LIGHTMAGENTA_EX + "\n" + ciphers[cipher])
    func = eval(ciphers_func_names[ciphers[cipher]].lower().replace(" ", "_") + "_cipher")
    text = input(Fore.GREEN + "Исходный текст (пусто - случайный набор символов): " + Fore.LIGHTGREEN_EX) or\
           ''.join(choice(ascii_letters + digits) for _ in range(100))
    if cipher:
        key = input(Fore.GREEN + "Ключ шифра (пусто, 0 или 1 - случайный набор букв/цифр): " + Fore.LIGHTGREEN_EX)
        key = randint(2, len(text)) if not cipher or cipher < 2 else "".join(choice(ascii_letters)
                                                                             for i in range(min(len(text), 25)))\
              if key == "" else int(key)
    print(func(text, key) if cipher else func(text))


input(Fore.LIGHTBLACK_EX + "\n\nПрограмма завершена. Нажмите <Enter>, чтобы выйти" + Fore.BLACK)
# python "G:\Мой Диск\Project\Code\main.py"

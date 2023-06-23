import brief, extended, with_libraries
from random import choice, randint
from string import ascii_letters, digits
from time import time


ciphers_names = {"Atbash": "Шифр Атбаш",
                 "Vigenere": "Шифр Виженера",
                 "Scytale": "Шифр Скиталы",
                 "Rail Fence": "Шифр ограничения рельса",
                 "Caesar": "Шифр Цезаря"}


def testing(cipher_name, type_one, only_this, libs):
    types = only_this if only_this else libs
    type_one = only_this if only_this else types[type_one]
    func_name = cipher_name.lower().replace(" ", "_") + "_cipher"
    func = eval(f'{type_one}.{func_name}')
    tested = testing_time(func, cipher_name)
    return tested


def testing_time(func, cipher_name):
    repeats, times = 10000, []
    for _ in range(repeats):
        start = round(time(), 8)
        string = ''.join(choice(ascii_letters + digits) for _ in range(1000))
        key = randint(0 if cipher_name not in ["Rail Fence", "Scytale"] else 2, 100) \
            if cipher_name != "Vigenere" else ''.join(choice(ascii_letters) for _ in range(8))
        func(string, key) if cipher_name != "Atbash" else func(string)
        end = round(time(), 8)
        times.append(end - start)
    return sum(times) / len(times)


def test(cipher_name, only_this, times, libs):
    tests = [testing(cipher_name, 0 if only_this else i, only_this, libs) for i in range(len(libs))]
    if not only_this:
        [times[idx].append(item) for item, idx in zip(tests, range(len(libs)))]
    else:
        print(f"{ciphers_names[cipher_name]}: {round(sum(i for i in tests) / len(tests), 8)}")


def go_test(func_name, repeats=1, only_this=""):
    libs = ["extended", "brief", "with_libraries"]
    times = [[], [], []]
    [test(func_name, only_this, times, libs) for _ in range(repeats)]
    print("\nCреднее время:")
    [print(libs[idx].capitalize() + ": " + str(round(sum(time_do)/len(time_do), 8)))
     for time_do, idx in zip(times, range(len(libs)))]

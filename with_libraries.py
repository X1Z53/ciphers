from codext.crypto.scytale import scytale_encode as scytale
from pythocrypt.rail_fence import encrypt as rail_fence
from python_master.ciphers.atbash import atbash
from python_master.ciphers.caesar_cipher import encrypt as caesar
from python_master.ciphers.vigenere_cipher import encryptMessage as vigenere


# Шифр Цезаря
def caesar_cipher(text, key):
    return caesar(text, key)


# Шифр Атбаш
def atbash_cipher(text):
    return atbash(text)


# Шифр ограждения рельса
def rail_fence_cipher(text, key):
    return rail_fence(text, key, False, False)


# Шифр Скилата
def scytale_cipher(text, key):
    return scytale(key)(text)[0]


# Шифр Виженера
def vigenere_cipher(text, key):
    return vigenere(key, text)

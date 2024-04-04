import secrets
import random
from string import ascii_letters, digits, punctuation

symbols = ascii_letters + digits + punctuation
symbol_list = [*symbols]
nam = 9999997999


def encryption(seed: int, mesage: str) -> str:
    n = seed

    seedIn = 37  # secrets.randbelow(n)

    key = n ^ seedIn

    random_symbol_list = [*symbols]

    random.seed(key)
    random.shuffle(random_symbol_list)

    autput = ""
    autput_list = []

    for num in range(len(mesage)):

        autput_list.append(random_symbol_list[num % len(random_symbol_list)])

    return autput_list


def decryption(seed: int, mesage: str) -> str:
    n = seed

    seedIn = 3

    key = n ^ seedIn

    random_symbol_list = [*symbols]

    random.seed(key)
    random.shuffle(random_symbol_list)

    autput = ""
    autput_list = []

    for num in range(len(mesage)):

        autput_list.append(symbol_list[num % len(symbol_list)])

    return autput_list


print(encryption(nam, "Hello W"))
print(decryption(nam, "17iCrb"))

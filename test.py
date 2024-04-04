# import random

# lista = [1, 2, 3, 4]

# seed = 1230
# random.seed(seed)

# random.shuffle(lista)

# print(lista)

from string import ascii_letters, digits, punctuation

symbol_list = ascii_letters + digits + punctuation

print([*symbol_list])

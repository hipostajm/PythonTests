import random

file = open("./Randomizer/Changed.txt", 'a')

file0 = open("./Randomizer/Text.txt", 'r')
file1 = open("./Randomizer/Changed.txt", 'w')

file0 = file0.read().split()

while len(file0)!=0:
    a = random.randint(0,len(file0)-1)
    file1.write(f"{file0[a]} ")
    del file0[a]
#Simple fibboncia numbers/phi generator


num_list = []

que = int(input("How many fibbonaci numbers: "))

for element in range(que):
    if len(num_list)  > 1:
        num_list.append(num_list[-1]+num_list[-2])
    elif len(num_list) == 1:
        num_list.append(1)
    elif len(num_list) == 0:
        num_list.append(0)

que2 = input('1 for fibbonaci numbers 2 for phi: ')

if que2 == '1':
    print(num_list)
elif que2 == '2' and num_list[-2] != 0:
    print(num_list[-1]/num_list[-2],'...')


#zapisywać to na tablicy
from string import *

SymbolList = ascii_letters + digits + punctuation
PassList=[]

#Its kinda like a zip bomb soo dont use to much for's

for element in SymbolList:

    Pass=element
    PassList.append(Pass)

    for element in SymbolList:

        Pass2=Pass+element
        PassList.append(Pass2)

        for element in SymbolList:

            Pass3=Pass2+element
            PassList.append(Pass3)

            #for element in SymbolList:
                #Pass4=Pass3+element
                #PassList.append(Pass4)
            
                #for element in SymbolList:
                    #Pass5=Pass4+element
                    #PassList.append(Pass4)

file = open("./Pass.txt", 'w')

for element in PassList:
    file.write(element+"\n")
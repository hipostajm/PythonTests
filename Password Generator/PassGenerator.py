from string import *
SymbolList = ascii_letters + digits + punctuation
PassList=[]
for i in SymbolList:
    Pass=''
    Pass=i
    PassList.append(Pass)
    for i in SymbolList:
        Pass2=Pass+i
        PassList.append(Pass2)
        for i in SymbolList:
            Pass3=Pass2+i
            PassList.append(Pass3)
            #for i in SymbolList:
                #Pass4=Pass3+i
                #PassList.append(Pass4)
                #for i in range(len(SymbolList)):
                    #Pass5=Pass4+SymbolList[i]
                    #PassList.append(Pass4)
            
                #Its kinda like a zip bomb soo dont use to much for's

#print(PassList)

file = open("./Pass.txt", 'w')

for i in PassList:
    file.write(i+"\n")
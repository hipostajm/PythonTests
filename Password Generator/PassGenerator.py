SymbolList=(' ',"a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0')
PassList=[]
for i in range(len(SymbolList)):
    Pass=''
    Pass=SymbolList[i]
    for i in range(len(SymbolList)):
        Pass2=Pass+SymbolList[i]
        PassList.append(Pass2)
        for i in range(len(SymbolList)):
            Pass3=Pass2+SymbolList[i]
            PassList.append(Pass3)
            for i in range(len(SymbolList)):
                Pass4=Pass3+SymbolList[i]
                PassList.append(Pass4)
                #for i in range(len(SymbolList)):
                    #Pass5=Pass4+SymbolList[i]
                    #PassList.append(Pass4)
#print(PassList)

file = open("Pass.txt", 'w')

for i in PassList:
    file.write(i+"\n")
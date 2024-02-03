from string import *

SymbolList = ascii_letters + digits + punctuation
file = open("./Pass.txt", 'w')
#Its kinda like a zip bomb soo dont use to much for's

for element in SymbolList:

    Pass=element

    file.write(Pass+"\n")

    for element in SymbolList:

        Pass2=Pass+element

        file.write(Pass2+"\n")

        for element in SymbolList:

            Pass3=Pass2+element

            file.write(Pass3+"\n")

            for element in SymbolList:
                Pass4=Pass3+element

                file.write(Pass4+"\n")
            
                for element in SymbolList:
                    Pass5=Pass4+element

                    file.write(Pass5+"\n")

import re
print("pre-compilador")

arq = open('exe.c', 'r')
arq2 = open('saida.c','w')

texto = arq.readlines()

saida = []
saida2 = []
fleg = False

print(len(texto))
for i in range(len(texto)) :
    if re.findall("//", texto[i]) == []:
        saida.append(texto[i])





for i in range(len(saida)) :
    if re.findall('\/\*', saida[i]) != []:
        fleg = True

    if not(fleg):
        saida2.append(saida[i])

    if re.findall("\*\/", saida[i]) != []:
        fleg = False

arq2.writelines(saida2)
arq2.close()
arq.close()

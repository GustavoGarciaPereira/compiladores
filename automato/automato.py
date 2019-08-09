
'''
1
2
3
4
5
'''


"""alfabeto = ['a','b']
estados = ['Q1','Q2','Q3']

estado_Ini = 'Q1'
estado_Fin = 'Q2' ## termo reconhecido

regras_tra = [
            {'a':q1,'b':q1},
            {'a':q1,'b':q2},
            {'a':-,'b':q2}
            ]
"""
regras_tra = {
    'q0': {'a':'q1','b':'q1'},
    'q1': {'a':'q1','b':'q2'},
    'q2': {'a':'-','b':'q2'}
}
print(regras_tra)
arq = open('confafd.txt', 'r')
texto = arq.readlines()


ler_regras = []
matriz_transicao = {}
regras = {}


for i in range(len(texto)) :
    if i == 0:
        print("alfa",texto[i])

    if i == 1:
        print("estados",texto[i])
    if i == 2:
        print("estado final",texto[i])
    if i == 3:
        print("estado inicial",texto[i])
    if i == 4:
        #print("regras de transicao",texto[i])
        ler_regras = texto[i]


print(ler_regras)

for i in ler_regras.split(','):
    regras[i.split(':')[1]] = i.split(':')[2]
    matriz_transicao[i.split(':')[0]] = regras
    print("Q1:::",i.split(':')[0])
    print("Q2:::",i.split(':')[1])
    print("Q3:::",i.split(':')[2])
    i.split(':')[0]

print(matriz_transicao)
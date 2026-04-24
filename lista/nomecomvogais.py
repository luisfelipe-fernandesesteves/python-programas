'''
escreva um programa que leia 5 nomes e armazene os em uma lista
'''

nomes = []

''' para i de 0 a 4, ou seja, 5 vezes '''
for i in range(5): 
    nome = input('Nome: ')
    nomes.append(nome)

print('--------------------')

''' para cada "nome" na lista de "nomes" '''
#declarando as vogais para verificar se o nome começa com uma vogal ou não
vogais = 'aeiouAEIOU'
# para nome na lista de nomes.
for nome in nomes:
    # [0] é a posição do primeiro caractere do nome, ou seja, a letra inicial
    # nome com a primeira letra do nome, verificando se ela está na string de vogais
    if nome[0] in vogais:
        print(f'Nome com vogais: {nome}')
    else:
        print(f'Nome sem vogais: {nome}')
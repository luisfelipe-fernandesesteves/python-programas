'''
escreva um programa que leia 5 nomes e armazene os em uma lista
'''

nomes = []
 # cria uma lista vazia chamada "nomes"


for i in range(5): 
   # range(5) gera números de 0 até 4
    # isso faz o laço repetir 5 vezes

    nome = input('Nome: ')
    nomes.append(nome)
    # append() adiciona o nome digitado dentro da lista "nomes"

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

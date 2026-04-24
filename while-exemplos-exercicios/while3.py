'''
Exercício 3 Soma acumulada
crie um programa que solicite números ao usuário até que ele digite 0
Ao final, exiba a soma de todos os números informados 
(desconsiderando o zero).
Exemplo:
Digite um número (0 para sair): 3 
Digite um número (0 para sair): 7
Digite um número (0 para sair): 2
Digite um número (0 para sair): 0
Soma total: 12'''

numero = int(input("Digite um número (0 para sair): "))
soma = 0
while numero != 0:
    soma += numero
    numero = int(input("Digite um número (0 para sair): "))
print("Soma total:", soma)

    
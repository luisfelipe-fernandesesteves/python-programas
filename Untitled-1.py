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

numero = int

#while = condição. ex: se numero for 0 o código executa X função
while numero > 0:
    numero = int(input("Digite um número (0 para sair): "))
    if numero > 0:
        soma = soma + numero
print("Soma total: ", soma)

    
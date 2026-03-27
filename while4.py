'''Exercício 4 Média de valores 
Escreva um programa que leia vários números informados pelo usuário. 
O programa deve encerrar quando o usuário digitar -1 e, ao final, calcular e exibir a média dos valores digitados 

(desconsiderando o -1). 
Exemplo: 
Digite um número (-1 para sair): 6 
Digite um número (-1 para sair): 8 
Digite um número (-1 para sair): 4 
Digite um número (-1 para sair): -1 
Média: 6.0
'''
numero = int(input("Digite um número (-1 para sair): "))
soma = 0

while numero != -1:
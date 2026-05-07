#definição da função
def diga_ola(nome):
    print(f'Olá, {nome}')
    
def obter_nome():
    nome = input('Nome: ')
    return nome
    
    
#MAIN - PRINCIPAL
i = 1
while i <= 3 :
    nome = obter_nome()
    diga_ola(nome)
    i+=1
# diga_ola() #chamada da função
# enquanto i for menor ou igual a 3 
# ele vai pedir seu nome e aparecer (olá, "nome_digitado")
# ou sejá, ele vai pedir seu nome 3 vezes

'''
Calculadora Simples

(X) imprimir menu com permissoes:
somar 2 numeros
subitrair 2 numeros
multiplicar 2 numeros
dividir 2 numeros
função controlador()

fluxo:
imprimir menu com as opções -->
imprimir para o usuario digitar 2 numeros -->
declarar variavel n1 e n2 com imput -->
input de opção -->
operações -->
imprimir resultados
'''

def menu():
    print('--- Menu ---')
    print('1 - ADIÇÃO')
    print('2 - SUBITRAÇÃO')
    print('3 - MULTIPLICAÇÃO')
    print('4 - DIVISÃO')
    #variavel opção dentro de DEF menu
    #só vai ser mostrada dentro de menu
    opcao = int(input('opção')) #variavel opcao recebe o valor digitado pelo usuario
    return opcao #vai retornar a opção digitada para o controlador

def entrada_dados():#vai ser reutilizada para n1 e n2
    print('--- entrada de dados ---')
    numero = int(input('numero: '))#variavel numero dentro de DEF entrada_dados
    return numero #vai retornar o numero digitado para o controlador

def adicao(n1, n2):#n1 e n2 são os numeros digitados pelo usuario
    print('--- adição ---')
    return n1+n2 #vai retornar a soma de n1 e n2 para o controlador

def subtracao(n1, n2): #n1 e n2 são os numeros digitados pelo usuario
    print('--- subtração--- ')
    return n1-n2 #vai retornar a subtração de n1 e n2 para o controlador

def multiplicacao(n1, n2): #n1 e n2 são os numeros digitados pelo usuario
    print('--- multiplicacao ---')
    return n1*n2 #vai retornar a multiplicação de n1 e n2 para o controlador

def divisão(n1, n2):#n1 e n2 são os numeros digitados pelo usuario
    print('--- divisão ---')
    return n1/n2 #vai retornar a divisão de n1 e n2 para o controlador

def inprimir(resultado):#resultado é o valor retornado pelo controlador
    print ('--- imprimir ---')
    print ('=======================')
    print (f'resultado {resultado}') #ELE PEGA RESULTADO DE CONTROLADOR E IMPRIME PARA O USUÁRIO
    print ('=======================')
    
def controlador(opcao, n1, n2): #opção é o valor retornado pelo menu, n1 e n2 são os valores retornados pela entrada de dados
    print ('--- controlador ---')
    if opcao == 1: #se a opção for 1, vai chamar a função adição e passar n1 e n2 como parametros
        resultado = adicao(n1, n2) #resultado é a variavel que vai receber o valor retornado pela função adição, que é a soma de n1 e n2
    elif opcao == 2: #se a opção for 2, vai chamar a função subtração e passar n1 e n2 como parametros
        resultado = subtracao(n1, n2) #resultado é a variavel que vai receber o valor retornado pela função subtração, que é a subtração de n1 e n2
    elif opcao == 3: #se a opção for 3, vai chamar a função multiplicação e passar n1 e n2 como parametros
        resultado = multiplicacao(n1, n2)
    elif opcao == 4:
        resultado = divisão(n1, n2)
    else:
        print('opção invalida')
    return resultado #vai retornar o resultado da operação escolhida para a função inprimir

#principal main
# é oque vai ser executado quando rodar o programa

#menu vai ser mostrado para o usuario
opcao = menu() #variavel opção recebe o valor retornado pelo menu, que é a opção escolhida pelo usuario
n1 = entrada_dados() #variavel n1 recebe o valor retornado pela função entrada_dados, que é o numero digitado pelo usuario
#reutilização de entrada de dados
n2 = entrada_dados() #variavel n2 recebe o valor retornado pela função entrada_dados, que é o numero digitado pelo usuario

resultado = controlador(opcao, n1, n2) #variavel resultado recebe o valor retornado pela função controlador, que é o resultado da operação escolhida pelo usuario
inprimir(resultado) #chama a função inprimir e passa o resultado como parametro, que é o valor retornado pela função controlador, que é o resultado da operação escolhida pelo usuario


        
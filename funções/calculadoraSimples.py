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
    opcao = int(input('opção'))
    return opcao

def entrada_dados():
    print('--- entrada de dados ---')
    numero = int(input('numero: '))
    return numero

def adicao(n1, n2):
    print('--- adição ---')
    return n1+n2

def subtracao(n1, n2):
    print('--- subtração--- ')
    return n1-n2

def multiplicacao(n1, n2):
    print('--- multiplicacao ---')
    return n1*n2

def divisão(n1, n2):
    print('--- multiplicacao ---')
    return n1/n2

def inprimir(resultado):
    print ('--- imprimir ---')
    print ('=======================')
    print (f'resultado {resultado}')
    print ('=======================')
    
def controlador(opcao, n1, n2):
    print ('--- controlador ---')
    if opcao == 1:
        resultado = adicao(n1, n2)
    elif opcao == 2:
        resultado = subtracao(n1, n2)
    elif opcao == 3:
        resultado = multiplicacao(n1, n2)
    elif opcao == 4:
        resultado = divisão(n1, n2)
    else:
        print('opção invalida')
    return resultado

#principal main
# é oque vai ser executado quando rodar o programa

#menu vai ser mostrado para o usuario
opcao = menu()
n1 = entrada_dados()
#reutilização de entrada de dados
n2 = entrada_dados()

resultado = controlador(opcao, n1, n2)
inprimir(resultado)


        
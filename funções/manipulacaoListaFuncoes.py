'''
qtd de alunos
lista notas
imprimir notas
calcular média
verificar quem está abaixo da média
lista com as notas abaixo da media
'''

# O 'def' (definition) serve para CRIAR uma função. 
# É como um bloco de código que fica guardado e só roda quando você o chama pelo nome.
def qtd_alunos():
    print('-- quantidade de alunos --')
    qtd = 0
    while qtd < 1:
        qtd = int(input('qtd de alunos: '))
        if qtd < 1:
            print('quantidade precisa ser MAIOR do que ZERO.')
    return qtd

def prencher_notas(qtd):
    print('-- preenchendo as notas... --')
    notas = [] # Cria uma lista vazia
    for i in range(qtd): # O 'range' serve para criar uma sequência de números. (lista de índices)
        nota = float(input(f'Nota do aluno {i+1}: '))
        notas.append(nota)
        # O 'append' serve para ADICIONAR um item ao final da lista.
        # Ele "anexa" o valor da variável 'nota' dentro da lista 'notas'.
    return notas
    
def imprimir_notas(notas):
    print('-- imprimindo as notas dos alunos... --')
    for i, nota in enumerate(notas, 1):
        # O 'enumerate' serve para enumerar os itens de uma lista.
        # Ele retorna dois valores a cada volta do laço: o ÍNDICE (posição) e o VALOR (item).

        
        # --- Traduzindo o que o enumerate faz por baixo dos panos: ---
        # Na 1ª volta: i = 1, nota = 8.5
        # Na 2ª volta: i = 2, nota = 5.0
        # Na 3ª volta: i = 3, nota = 9.0
        print(f'Aluno {i}: {nota}')

def calcular_media(notas):
    total_notas = sum(notas) # Soma todos os valores da lista
    media = total_notas / len(notas)
    # O 'len' (length) serve para medir o TAMANHO da lista.
    # Se a lista tem 5 notas, len(notas) será igual a 5.
    print(f"A média da turma é: {media:.2f}") # O :.2f é uma formatação que limita a exibição da média a 2 casas decimais.
    return media

def verificar_abaixo_media(notas):
    print('-- alunos abaixo da média (6.0) --')
    alunos_abaixo = []
    for i, nota in enumerate(notas, 1): # O 'enumerate' aqui é usado novamente para obter o índice (i) e o valor (nota) de cada item na lista 'notas'.
        if nota < 6:
            print(f'Aluno {i} com nota {nota} está abaixo da média.')
            alunos_abaixo.append(nota) # O 'append' aqui é usado para adicionar a nota do aluno que está abaixo da média à lista 'alunos_abaixo'.
    return alunos_abaixo

# --- Fluxo Principal ---
# def main() é a função principal que orquestra a execução do programa, 
# chamando as outras funções em sequência para realizar as tarefas necessárias.
def main():
    qtd = qtd_alunos()
    lista_notas = prencher_notas(qtd)
    imprimir_notas(lista_notas)
    media_final = calcular_media(lista_notas)
    verificar_abaixo_media(lista_notas)

main()

"""
============================================================
O QUE CADA COMANDO FAZ NO PYTHON:
============================================================

1. def (Definition):
   Serve para CRIAR uma função. É como dar um nome a um 
   conjunto de instruções para usá-las depois apenas 
   chamando esse nome.
   Ex: def calcular_total():

2. append (Anexar):
   É um comando de LISTAS. Ele serve para colocar um novo 
   dado no final de uma lista que já existe.
   Ex: lista.append(valor) -> [item1, item2, VALOR]

3. len (Length):
   Serve para contar o TAMANHO de algo. Se usado em uma 
   lista, ele diz quantos itens tem lá dentro.
   Ex: len([10, 20, 30]) retorna 3.

4. .2f (Float Formatting):
   Usado dentro de strings (f-strings) para limitar as 
   casas decimais de um número. O '2' indica duas casas.
   Ex: f"{3.1415:.2f}" vira "3.14".

5. enumerate (Enumerar):
   Serve para percorrer uma lista recebendo ao mesmo tempo 
   o ÍNDICE (a contagem) e o VALOR (o dado). Evita ter 
   que criar contadores manuais como 'i = i + 1'.
   Ex: for i, nota in enumerate(notas, 1):
============================================================
"""

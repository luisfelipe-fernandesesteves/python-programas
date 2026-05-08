def qtd_alunos():
    print('-- quantidade de alunos --')
    qtd = 0
    while qtd < 1:
        qtd = int(input('qtd de alunos: '))
        if qtd < 1:
            print('quantidade precisa ser MAIOR do que ZERO: 0')
    return qtd

#qtd define quantas vezes vai rodar (quantos alunos tem)
def prencher_notas(qtd):
    print('--preenchendo as notas...--')
    notas = []
    for i in range(qtd):
        print(f'aluno {i+1}:')
        nota = float(input('NOTA:'))
        notas.append(nota)
    return notas
    
def imprimir_notas(notas):
    print('--imprimindo as notas dos alunos...--')
    i = 1
    for nota in notas:
        print(f'aluno{i}: ')
        print(f'nota:{nota}')
        i += 1
#principal, onde vai rodar
qtd = qtd_alunos()
lista_notas = prencher_notas(qtd)
imprimir_notas(lista_notas)

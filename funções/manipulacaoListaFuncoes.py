def qtd_alunos():
    print('-- quantidade de alunos --')
    qtd = 0
    while qtd < 1:
        qtd = int(input('qtd de alunos: '))
        if qtd < 1:
            print('quantidade precisa ser MAIOR do que ZERO: 0')
    return qtd

def prencher_notas(qtd):
    print('--preenchendo as notas...--')
    notas = []
    for i in range(qtd):
        nota = float(input('NOTA:'))
        notas.append(nota)


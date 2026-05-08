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
    notas = []
    for i in range(qtd):
        nota = float(input(f'Nota do aluno {i+1}: '))
        notas.append(nota)
    return notas
    
def imprimir_notas(notas):
    print('-- imprimindo as notas dos alunos... --')
    for i, nota in enumerate(notas, 1):
        print(f'Aluno {i}: {nota}')

def calcular_media(notas):
    total_notas = sum(notas) # Soma todos os valores da lista
    media = total_notas / len(notas)
    print(f"A média da turma é: {media:.2f}")
    return media

def verificar_abaixo_media(notas):
    print('-- alunos abaixo da média (6.0) --')
    alunos_abaixo = []
    for i, nota in enumerate(notas, 1):
        if nota < 6:
            print(f'Aluno {i} com nota {nota} está abaixo da média.')
            alunos_abaixo.append(nota)
    return alunos_abaixo

# --- Fluxo Principal ---
def main():
    qtd = qtd_alunos()
    lista_notas = prencher_notas(qtd)
    imprimir_notas(lista_notas)
    media_final = calcular_media(lista_notas)
    verificar_abaixo_media(lista_notas)

main()

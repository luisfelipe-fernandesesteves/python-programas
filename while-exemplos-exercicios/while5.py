'''📌 Exercício 5 Validação de senha 
Crie um programa que solicite ao usuário uma senha. 
Enquanto a senha digitada estiver incorreta
o programa deve continuar pedindo novamente. 
Quando o usuário acertar, exiba uma mensagem de acesso permitido.

--Regras: Defina uma senha fixa no código 
(por exemplo: 1234) 
Utilize while para repetir até acertar 
Exemplo:
Digite a senha: 1111 
Senha incorreta! 
Digite a senha: 1234 
Acesso permitido!
Bora praticar, galera! Ótimos estudos!!!
'''
senha_correta = "1234"
# O programa continuará solicitando a senha até que o usuário acerte a senha correta.
# O loop while é usado para repetir a solicitação de senha até que a condição seja satisfeita (senha correta).
#WHILE TRUE em Python é uma estrutura de controle de fluxo que cria um loop infinito.
# nao utilize o while true, pois ele pode causar um loop infinito se não for controlado adequadamente.
while True:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
        print("Acesso permitido!")
        #break é uma palavra-chave em Python que é usada para sair imediatamente de um loop, seja ele um loop for ou while. Quando o programa encontra a instrução break dentro de um loop, ele interrompe a execução do loop e continua com o código que vem após o loop.
        break
    else:
        print("Senha incorreta! Tente novamente.")
        
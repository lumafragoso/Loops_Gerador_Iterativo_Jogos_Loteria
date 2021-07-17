import random
condicao = True
while condicao:
    tipo = int(input('Escolha o tipo de jogo:\n(1) 6 dezenas, (2) 7 dezenas, (3) 8 dezenas ou (4) Sair:'))
    modo = int(input('Escolha do modo do jogo:\n(1) Jogo aleatorio ou (2) Manual:'))
    if tipo == 1:
        if modo == 1:
            s = ""
            for i in range(6):
                s += str(random.randint(1, 60)) + " "
            print('Jogo {}'.format(s))
        elif modo == 2:
            n1, n2, n3, n4, n5, n6 = input('Digite o jogo, entre cada número digite um espaço:').split()
        print('Jogo confirmado!')
    elif tipo == 2:
        if modo == 1:
            s = ""
            for i in range(7) :
                s += str(random.randint(1, 60)) + " "
            print('Jogo {}'.format(s))
        elif modo == 2:
            n1, n2, n3, n4, n5, n6, n7 = input('Digite o jogo, entre cada número digite um espaço:').split()
        print('Jogo confirmado!')
    elif tipo == 3:
        if modo == 1:
            s = ""
            for i in range(8) :
                s += str(random.randint(1, 60)) + " "
            print('Jogo {}'.format(s))
        elif modo == 2:
            n1, n2, n3, n4, n5, n6, n7, n8 = input('Digite o jogo, entre cada número digite um espaço:').split()
        print('Jogo confirmado!')
    elif tipo == 4:
        print('Saindo...')
        condicao = False

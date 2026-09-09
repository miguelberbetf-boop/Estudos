import random
while True:
    print("    VAMOS JOGAR PAR OU ÍMPAR?   ")
    re1 = input('[S/N]')
    if re1 == 'S':
        jogador = int(input('Digite um numero'))
        jogador1 = input('[Par ou Impar]')
        maquina = random.randint
        print(maquina)
        if jogador1 == 'Par':
            P = (jogador + maquina)//2
            if P == 0:
                print('Vc ganhou')
            else:
                print('vc perdeu')
                jgdnv = input('quer joga denovo? [S/N]')
                if jgdnv == 'S':
                    break
                else:
                    break
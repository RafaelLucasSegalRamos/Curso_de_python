from time import sleep

try:
    print('\033[96mOlhe! Já vai começar o estouro de fogos de artifício\033[m!')
    print('Vamos fazer contagem regressiva!')
    for i in range(10, -1, -1):
        print(i)
        sleep(1)
    print('\033[92m\nFELIZ ANO NOVO!!!\033[m')


except KeyboardInterrupt:
    print('\033[91m\nO usuário interrompeu o progama.')

except:
    print('\033[91m\nOcorreu um erro não identificado.')

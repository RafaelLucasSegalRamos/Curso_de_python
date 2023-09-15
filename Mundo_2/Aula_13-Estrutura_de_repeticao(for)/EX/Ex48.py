from time import sleep

try:
    print("Aqui estão os números impares que são multiplos de 3, entre 1 e 500:")
    for i in range(0, 501, 3):
        if i % 2 == 1:
            print(i, end=" ")
        sleep(0.25)


except KeyboardInterrupt:
    print('\033[91m\nO usuário interrompeu o progama.')

except:
    print('\033[91m\nOcorreu um erro não identificado.')

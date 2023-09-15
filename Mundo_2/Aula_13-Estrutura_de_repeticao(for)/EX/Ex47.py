from time import sleep

try:
    print("Aqui estão os números pares entre 1 e 50:")
    for i in range(2, 51, 2):
        print(i, end=" ")
        sleep(0.25)


except KeyboardInterrupt:
    print('\033[91m\nO usuário interrompeu o progama.')

except:
    print('\033[91m\nOcorreu um erro não identificado.')

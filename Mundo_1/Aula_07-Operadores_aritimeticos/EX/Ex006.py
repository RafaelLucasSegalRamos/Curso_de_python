try:
    while True:
        num = str(input('Digite um valor aleatório: '))
        if num.isnumeric():
            break
        else:
            print(f'\033[91mO valor {num}, não é um valor inteiro!Tente denovo!\033[0m')
    numero = int(num)

    print(f'O valor \033[96m{numero * 2}\033[0m é o dobro de \033[93m{numero}\033[0m')
    print(f'O valor \033[96m{numero * 3}\033[0m é o triplo de \033[93m{numero}\033[0m')
    print(f'O valor \033[96m{numero ** (1/2):.4f}\033[0m é a raiz quadrada de \033[93m{numero}\033[0m')

except:
    print('\033[91mAlgo deu Errado! Ou o usuário parou o progama a força.')
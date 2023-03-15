try:
    while True:
        numero = str(input('Digite um número inteiro: '))
        if numero.isnumeric():
            break
        else:
            print('\033[31mO valor digitado, não é númerico ou inteiro!\033[0m')

    num = int(numero)

    mai = num + 1
    men = num - 1

    print(f'A sequência do número \033[95m{num}\033[0m é: '
          f'\033[96m {men} \033[0m > \033[95m {num} \033[0m > \033[96m {mai} \033[0m')

except:
    print('\033[31m Algo deu errado ou o usuário parou o progama.')
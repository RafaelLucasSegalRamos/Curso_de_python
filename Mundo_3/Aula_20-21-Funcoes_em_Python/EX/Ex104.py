def leiaint(num):
    while True:
        n = str(input(num))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return n


nume = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {nume}.')

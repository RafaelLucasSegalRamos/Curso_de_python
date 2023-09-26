# fazendo o exercicio 077 do curso de python do canal Curso em Video

while True:
    try:
        num_a = 0
        tupla = (str(input('Digite uma palavra: ')),
                    str(input('Digite outra palavra: ')),
                    str(input('Digite mais uma palavra: ')),
                    str(input('Digite a última palavra: ')))
        print(f'Você digitou as palavras {tupla}')

        print(f'A letra "a" apareceu na posição ', end='')
        for n in range(0, len(tupla)):
            for j in range(0, len(tupla[n])):
                if tupla[n][j].count('a') > 0:
                    print(n+1, end=' ')
                    num_a += 1
        print("\nA letra 'a' apareceu {} vezes".format(num_a))
        print('As vogais digitadas foram: ', end='')
        for n in tupla:
            for letra in n:
                if letra in 'aeiou':
                    print(letra, end=' ')
        print()


        while True:
            continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
            if continuar in 'SN':
                break
            else:
                print('\033[91mTente novamente. ', end='')
        if continuar == 'N':
            break


    except KeyboardInterrupt:
        print('\033[91mO usuário decidiu parar o programa.\033[m')
        break
    except Exception as erro:
        print(f'\033[91mO erro que aconteceu foi {erro}\033[m')
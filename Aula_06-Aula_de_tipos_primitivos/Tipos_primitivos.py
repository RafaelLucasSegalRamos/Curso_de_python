try:
    n1 = int(input('Coloque a primeira nota do aluno:\n'))

    n2 = int(input('Coloque a segunda nota do aluno:\n'))

    #  print(f'O valor do primeiro número é Inteiro? {n1.isnumeric()}')
    #  print(f'O valor do segundo número é Inteiro? {n2.isnumeric()}')

    m = (n1 + n2) / 2

    print(f'A média do aluno foi de {m}.')

except:
    print('\033[31mAlgo deu errado, ou o usuário parou o progama.')

import math

try:
    n1 = int(input('Coloque a primeira nota do aluno:\n'))

    n2 = int(input('Coloque a segunda nota do aluno:\n'))

    #  print(f'O valor do primeiro número é Inteiro? {n1.isnumeric()}')
    #  print(f'O valor do segundo número é Inteiro? {n2.isnumeric()}')

    print(f'A soma entre {n1} e {n2} é {n1+n2}')
    print(f'A subtração entre {n1} e {n2} é {n1-n2}')
    print(f'A multiplicação entre {n1} e {n2} é {n1*n2}')
    print(f'A divisão entre {n1} e {n2} é {n1/n2:.3f}')
    # Utilizando o {:.3f} o número de casas decimais que apareceram no final é 3,
    # por exemplo, uma dizima periodica de 1.33333... se torna 1.333,
    # pois são três pontos flutuantes(float) depois do ponto.
    print(f'A exponenciação entre {n1} e {n2} é {n1**n2}', end=' ')
    # Utilizando a função end='' é possivel definir como a frase termina,
    # e podendo fazer a junção de dois print que não fazem parte da mesma linha
    print(f'O resto da divisão entre {n1} e {n2} é {n1%n2}')
    print(f'O resultado da divisão (em número inteiro) entre {n1} e {n2} é {n1//n2}')
    print(f'O resultado da divisão (em número inteiro) entre {n1} e {n2} é {math.pi:>^80}')
    # na chave quando for colocar uma variavel no print é possivel mudar o jeito que a variavel aparece, por
    # é possivel forçar a raiz quadrada transformando a pontecia em fração, exemplo 9**2 == 81, 81**(1/2) == 9

except:
    print('\033[31mAlgo deu errado, ou o usuário parou o progama.')

def notas(showSituacao=True):
    """
    -> Função para analisar notas e situações de vários alunos.

    :param showSituacao: (Optional) This one is for the teacher or the user to choose if he wants to see the situation of the student or not.
    :return: Returns a dictionary with the information about the class.
    """
    notas = []
    s = 0
    while True:
        nota = float(input('Digite uma nota: '))
        notas.append(nota)
        while True:
            resp = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
            if resp in 'SN':
                break
        if resp == 'N':
            break

    for pos, i in enumerate(notas):
        if pos == 0:
            maior = i
            menor = i
        elif i > maior:
            maior = i
        elif i < menor:
            menor = i
        s += i
    media = s / len(notas)
    if showSituacao:
        if media < 5:
            situacao = 'RUIM'
        elif media < 7:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'BOA'
        infor = {'Numero de notas': len(notas), 'Maior nota': maior, 'Menor nota': menor, 'Média': media,
             'Situação': situacao}
    else:
        infor = {'Numero de notas': len(notas), 'Maior nota': maior, 'Menor nota': menor, 'Média': media}

    return infor


print(notas())
print(notas(False))

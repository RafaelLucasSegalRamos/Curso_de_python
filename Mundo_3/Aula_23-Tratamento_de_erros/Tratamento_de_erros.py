try:
    n = int(input('Digite um número: '))
    """print(f'Você digitou o número {n}')"""

except ValueError:
    print('Valor inválido!')

except Exception as erro:
    print(f'Erro: {erro.__class__}')

else:
    print(f'Você digitou o número {n}')

finally:
    print('Fim do programa!')
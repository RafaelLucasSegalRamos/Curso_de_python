# import ***; é para importar uma cadeia de funções
# from *** import * é para importar apenas uma função de um módulo

# import math importa o modulo da matemática

import math

n1 = float(input('Digite um valor a ser analizado: '))

print(f'O número {n1} arrendodado para cima é {math.ceil(n1)}')
print(f'O número {n1} arrendodado para baixo é {math.floor(n1)}')
print(f'O número {n1} sem nenhum valor depois da virgula é {math.trunc(n1)}')
print(f'O número {n1} ao quadrado é (utilizando o modulo de math.pow(): {math.pow(n1, 2)}')
print(f'O número {n1} ao quadrado é (utilizando o modulo de math.sqrt(): {math.sqrt(n1):.2f}')
print(f'O fatorial do número {n1} é {math.factorial(n1):.2f}')


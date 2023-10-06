from Ex107 import Ex107
from modulos.moedas.moedas import moeda

p = float(input('Digite o preço: R$'))
Ex107(p)
print(f'O valor escrito é {moeda(p)}')

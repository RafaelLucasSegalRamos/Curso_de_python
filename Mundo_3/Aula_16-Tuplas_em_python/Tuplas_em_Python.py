tupla = tuple()
tupla = ()
tupla = ('um')  # Tupla com um elemento
tupla1 = ('um', "dois")  # Tupla com vários elementos, e com tipos diferentes
tupla2 = (1, 2)
tupla3 = tupla1 + tupla2  # Tupla com elementos de outras tuplas
print(tupla3)

# Tuplas são imutáveis, ou seja, não podemos adicionar ou remover elementos

try:
    tupla[0] = 'novo'  # Error
except TypeError as erro:
    print(erro)
# Tuplas são indexadas, ou seja, podemos acessar os elementos através de índices
# Tuplas aceitam slicing
print()
lanches = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
texto = "teste"

for c in lanches:
    print(f"Eu vou comer {c}")

print('')
for i, pos in enumerate(lanches):
    print(f"Eu vou comer {pos} na posição {i}")

print(lanches[::-1])
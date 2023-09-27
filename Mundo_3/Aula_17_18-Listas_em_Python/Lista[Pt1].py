lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim'] # Isto é uma lista, funciona de um jeito meuito parecido com uma tupla, mas é mutável

# exemplo
print(lanche) # Aqui eu estou printando o índice 0 da lista lanche
lanche[3] = 'Sorvete' # Aqui eu mudei o valor do índice 3, que era pudim, para sorvete, o que uma tupla não permite
print(lanche)

# na lista podemos tambem adicionar valores

lanche.append('Cookie') # Aqui eu adicionei o valor 'Cookie' na lista lanche
print(lanche)

# podemos adicionar valores em qualquer posição

lanche.insert(0, 'Cachorro quente') # Aqui eu adicionei o valor 'Cachorro quente' na posição 0 da lista lanche
print(lanche)

# podemos remover valores

del lanche[3] # Aqui eu removi o valor da posição 3 da lista lanche
print(lanche)
lanche.pop(4) # Aqui eu removi o valor da posição 3 da lista lanche, da mesma forma que o del
print(lanche)
# Caso o .pop() não possua valor dentro dos parênteses, ele irá remover o último valor da lista
lanche.remove('Sorvete') # Aqui eu removi o valor 'Pizza' da lista lanche
print(lanche)

lista2 = [2, 5, 9, 1]
print(lista2)
lista2.sort() # Aqui eu ordenei a lista2
print(lista2)
lista2.sort(reverse=True) # Aqui eu ordenei a lista2 de forma reversa
print(lista2)
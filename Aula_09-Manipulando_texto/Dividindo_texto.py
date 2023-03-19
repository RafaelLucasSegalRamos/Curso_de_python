texto = 'Curso em video Python'

print(f'O texto {texto} fica assim dividido: {texto.split()}')
# O metodo .split() divide as palavras de uma string em diferentes string e as agrupa em uma lista.
# print(texto.split(maxsplit=0)) Utilizando o maxsplit=1 é possivel definir quantas vezes o texto será dividido
# print(texto.split(sep='em')) Utilizando o sep='' é possivel determinar onde exatamente acontecerá a divisão
# Exemplo print(texto.split(sep='em')) == ['Curso ', ' video Python']
print(f'O texto {texto} fica assim dividido: {"-".join(texto.split())}')
# Neste exemplo acima o '-'.join() coloca o '-' entre os itens da lista.
print('-'.join(texto))
# Já neste exemplo acima o '-'.join() coloca o '-' entre os caracteres da string .

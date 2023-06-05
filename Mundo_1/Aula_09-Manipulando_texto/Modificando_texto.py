texto = 'Curso em video Python'

print(texto[9])  # Fatiação de um unico digito, ou unico item
print(texto[9:14])  # Fatiação de um caracter (ou item) até outro,
# sendo que o segundo valor tem que ser um a mais do que o final desejado.
print(texto[9:21:2])  # Fatiação de um caracter (ou item) até outro,
# mas o dois por ultimo significa que será pego o caractere de 2 em 2
print(texto[:5])  # Fatiação que começa no 0 e termina no número pré-determinado, no exemplo: '5'
print(texto[15:])  # Fatiação que começa em um ponto pré-determindo e acaba no final desta string
print(texto[::2])  # Fatiação que começa do inicio ao fim mas pega os caracteres de 2 em 2

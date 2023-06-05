texto = 'Curso em video Python'

print(f'A largura do texto "{texto}" é {len(texto)} letras/caracteres')
# O len() mostra quantos caracteres/itens o texto/lista tem
print(f'O texto "{texto}" tem {texto.count("o")} letras "o"')
# O x.count() pode contar quantos tipos caracteres iguais, ou conjunto de caracteres iguais, tem em uma string
# Sendo possivel colocar limitações onde a função busca,
# fazendo: texto.count('o', 0, 13) sendo 0 o inicio e 13 o fim
print(f'A parte do texto onde está escrto "deo" começa no caractere {texto.find("deo")}')
# Utilizando o x.find() é possivel descobrir se na sentença existe alguma parte do texto solicitado,
# e quando o texto solicitado não existe ele retorna o valor -1
print(f'Na frase {texto} existe a palavra "Curso"? {"Curso" in texto}')
# Utilizando a propriedade 'in' podemos retornar um Valor True ou False
print(texto.replace('Python', 'Android'))
# tm = texto.replace(' ', 'teste') mas utilizando uma variavel para receber este valor,
# esta variavel então terá a mudança que foi definida
# replace muda como aparecerá em um print, mas o texto não terá mudado de fato.
print(f'A frase em letras maiusculas é :{texto.upper()}\nEnquanto isso está frase em minusculas é: {texto.lower()}')
# Pelo que o print descreve é auto-explicativo.
print(f'E aqui está é o texto com a primeira letra maiuscula: {texto.capitalize()}')
print(f'E de um jeito parecido, este é o texto com as primeiras letras maiusculas: {texto.title()}')

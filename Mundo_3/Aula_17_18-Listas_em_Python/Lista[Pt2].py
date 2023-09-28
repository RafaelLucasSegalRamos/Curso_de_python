dados = list()
pessoas = list()

dados.append('Pedro')
dados.append(25)

print(dados[0], dados[1])

pessoas.append(dados[:])
pessoas.append(['Maria', 19])
pessoas.append(['João', 32])

print(pessoas)
print(pessoas[0][0], pessoas[1][1], pessoas[2][0], pessoas[1])


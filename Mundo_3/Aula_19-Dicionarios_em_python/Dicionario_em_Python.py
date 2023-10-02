dici = {
        "nome": "Pedro",
        "idade": 25
        }  # Dicionário com chave e valor, chaves são parecidos com listas, mas não possui índices,
# então podemos colocar chaves de qualquer tipo, como strings, números, etc. Por exemplo a chave "nome" possui o valor "Pedro".

print(dici["nome"])  # Para acessar o valor de uma chave, basta colocar o nome do dicionário e entre colchetes o nome da chave.

dici["sexo"] = "M"  # Para adicionar um novo elemento ao dicionário, basta colocar o nome do dicionário, entre colchetes
print(dici)
del dici["idade"]  # Para deletar um elemento do dicionário, basta colocar o nome do dicionário, entre colchetes
print(dici)
print(dici.values()) # Para mostrar todos os valores do dicionário, basta colocar o nome do dicionário e ".values()".
print(dici.keys())  # Para mostrar todas as chaves do dicionário, basta colocar o nome do dicionário e ".keys()".
print(dici.items())  # Para mostrar todos os itens do dicionário, basta colocar o nome do dicionário e ".items()".

estado = dict()  # Para criar um dicionário vazio, basta colocar o nome do dicionário e "dict()".
brasil = list()  # Para criar uma lista vazia, basta colocar o nome da lista e "list()".
for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())  # Para adicionar um dicionário a uma lista, basta colocar o nome da lista e ".append()"
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    print()

